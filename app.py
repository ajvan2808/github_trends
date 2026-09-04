from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/trending")
def get_trending():
    duration = request.args.get("duration", "weekly")
    limit = int(request.args.get("limit", 10))
    language = request.args.get("language", "")

    try:
        from gh_service import fetch_trending_repos
        repos = fetch_trending_repos(duration=duration, limit=limit, language=language)
        return jsonify(repos)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    