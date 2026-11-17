import os
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests
from dotenv import load_dotenv

load_dotenv()

DURATION_DAYS = {
    "daily": 1,
    "weekly": 7,
    "monthly": 30,
    "yearly": 365,
}

# In-memory TTL cache: {cache_key: (timestamp, items)}
_CACHE: dict[str, tuple[float, list]] = {}
CACHE_TTL_SECONDS = 300  # 5 minutes


class GitHubAPIError(Exception):
    """Base GitHub API exception."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code


class GitHubRateLimitError(GitHubAPIError):
    """Raised when GitHub rate limit is exceeded (HTTP 403 / 429)."""
    def __init__(self, message: str = "GitHub API rate limit exceeded."):
        super().__init__(message, status_code=429)


def _get_start_date(duration: str = "weekly") -> str:
    days = DURATION_DAYS.get(duration.lower(), 7)
    start_date = datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh")) - timedelta(days=int(days))
    return start_date.strftime("%Y-%m-%d")


def fetch_trending_repos(duration: str = "weekly", limit: int = 10, language: str = "") -> list:
    cache_key = f"{duration.lower()}:{limit}:{language.lower().strip()}"
    now = time.time()

    # 1. Return fresh cached response if available
    if cache_key in _CACHE:
        cached_time, cached_items = _CACHE[cache_key]
        if now - cached_time < CACHE_TTL_SECONDS:
            return cached_items

    start_date = _get_start_date(duration)
    query = f"created:>={start_date}"
    if language:
        query += f" language:{language.strip()}"

    headers = {
        "User-Agent": "GitPulse-App/1.0",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    gh_token = os.getenv("GITHUB_TOKEN")
    if gh_token:
        headers["Authorization"] = f"Bearer {gh_token}"

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        # Handle rate limiting (403 or 429)
        if response.status_code in (403, 429):
            err_msg = response.json().get("message", "API rate limit exceeded") if response.content else "API rate limit exceeded"
            
            # If we have any stale cache for this key, serve it gracefully
            if cache_key in _CACHE:
                _, stale_items = _CACHE[cache_key]
                print(f"[WARN] GitHub rate limit hit ({err_msg}). Serving cached results.")
                return stale_items

            raise GitHubRateLimitError(
                f"GitHub API rate limit reached ({err_msg}). "
                "Please add a GITHUB_TOKEN environment variable in Render or .env file to get 5,000 req/hr."
            )

        response.raise_for_status()
        items = response.json().get("items", [])
        
        # Save to cache
        _CACHE[cache_key] = (now, items)
        return items

    except requests.exceptions.RequestException as e:
        # Fallback to stale cache on network failure
        if cache_key in _CACHE:
            _, stale_items = _CACHE[cache_key]
            print(f"[WARN] Network error ({e}). Serving cached results.")
            return stale_items
            
        print(f"Error fetching trending repositories: {e}")
        raise GitHubAPIError(f"Network error while reaching GitHub API: {e}", status_code=502)
