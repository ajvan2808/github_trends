# ⚡ GitPulse - GitHub Trending CLI & Web Dashboard

[project URL]((https://github.com/ajvan2808/github_trends))

**GitPulse** is a dual-interface application (CLI + Web Dashboard) that interacts with the GitHub REST API to track, filter, and display top trending open-source repositories in real time based on star velocity, timeframe, and language.

---

## ✨ Features

### 🖥️ 1. Powerful Terminal CLI (`cli.py`)
- Built with **Typer** and **Rich** for high-density, beautifully styled terminal output.
- Custom options for timeframe: `--duration` (`daily`, `weekly`, `monthly`, `yearly`).
- Result limit control (`--limit`) and language filtering (`--language`).
- Auto-formatted tables with rank badges, repository descriptions, star counts, fork metrics, and direct links.

### 🌐 2. Interactive Web Dashboard (`app.py` & `templates/index.html`)
- Built with **Flask** backend and a dark-mode **Obsidian Telemetry** UI styled with **Tailwind CSS**.
- Design converted directly from **StitchMCP** project `1542633312510810563`.
- Dynamic live filtering by duration (`Today`, `This Week`, `This Month`, `This Year`), programming language, and search queries.
- Metric indicators: Live API status,Loaded Repos count ticker, Language distribution breakdown, and SVG trend sparklines.

### 🔌 3. Shared Core API Client (`gh_service.py`)
- Solves GitHub REST API search query building (`created:>=YYYY-MM-DD sort:stars`).
- Includes automatic handling of GitHub API rate limits (60 req/hr unauthenticated or 5,000 req/hr with `GITHUB_TOKEN`).

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+** installed.

### 2. Setup Environment & Dependencies
Clone or navigate to the repository and activate your virtual environment:

```bash
cd github_trends

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux

# Install requirements
pip install requests typer rich flask gunicorn python-dotenv
```

*(Optional)* Set your GitHub Personal Access Token to avoid rate limits:
```bash
export GITHUB_TOKEN="your_personal_access_token"
```

---

## 💻 Usage

### Running the CLI Tool

Fetch trending repositories from your terminal:

```bash
# Default (Weekly, Top 10)
python cli.py

# Custom duration and limit
python cli.py --duration monthly --limit 5

# Filter by programming language
python cli.py --duration weekly --limit 10 --language python
```

#### CLI Help Options:
```bash
python cli.py --help
```

---

### Running the Web Dashboard

Start the Flask development server:

```bash
python app.py
```

Open your browser and navigate to:
**`http://127.0.0.1:5000`**

---

## ☁️ Deployment on Render

This project is ready for deployment on [Render](https://render.com/) for free.

1. Push your repository to GitHub.
2. Log into Render and click **New +** -> **Web Service**.
3. Connect your repository and configure:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt` (or `pip install .`)
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`
4. *(Optional)* Add environment variable `GITHUB_TOKEN` under Environment Variables.
5. Click **Create Web Service**.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask, Typer, Rich, Requests, Gunicorn
- **Frontend**: HTML5, Tailwind CSS (via CDN), Vanilla JavaScript, Material Symbols
- **Design System**: GitPulse / Obsidian Telemetry via StitchMCP
- **API**: GitHub REST API v3

---

## 📄 License

MIT License - Feel free to use and modify for your learning journey!

