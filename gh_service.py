import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests

DURATION_DAYS = {
    "daily": 1,
    "weekly": 7,
    "monthly": 30,
    "yearly": 365,
}


def _get_start_date(duration: str = "weekly"):
    days = DURATION_DAYS.get(duration.lower(), "7")
    start_date = datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh")) - timedelta(days=int(days))
    return start_date.strftime("%Y-%m-%d")


def fetch_trending_repos(duration: str = "weekly", limit: int = 10, language: str = "") -> list:
    start_date = _get_start_date(duration)
    query = f"created:>={start_date}"
    query += f" language:{language}" if language else ""

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    gh_token = os.getenv("GITHUB_TOKEN")
    if gh_token:
        headers["Authorization"] = f"Bearer {gh_token}"

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query, # required search query
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code == 403:
            raise Exception("API rate limit exceeded or access forbidden. " \
            "Please try again later or add a GITHUB_TOKEN.")  # noqa: TRY002

        response.raise_for_status()
        return response.json().get("items", [])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending repositories: {e}")
        return []