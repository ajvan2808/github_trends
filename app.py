import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/trending")
def get_trending():
    duration = request.args.get("duration", "weekly")
    try:
        limit = max(1, min(int(request.args.get("limit", 10)), 100))
    except (ValueError, TypeError):
        limit = 10
    language = request.args.get("language", "")

    try:
        from gh_service import fetch_trending_repos, GitHubAPIError
        repos = fetch_trending_repos(duration=duration, limit=limit, language=language)
        return jsonify(repos)
    
    except GitHubAPIError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    