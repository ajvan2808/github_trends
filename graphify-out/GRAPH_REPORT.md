# Graph Report - github_trends  (2026-11-17)

## Corpus Check
- 6 files · ~4,985 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 3, .example 1, .lock 1)

## Summary
- 65 nodes · 78 edges · 9 communities (4 shown, 5 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e2e8a04c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide
- ⚡ GitPulse - GitHub Trending CLI & Web Dashboard
- gh_service.py
- GitHubAPIError
- app.py
- cli.py
- 2. Understanding the GitHub API
- ✨ Features
- github-trends

## God Nodes (most connected - your core abstractions)
1. `fetch_trending_repos()` - 11 edges
2. `🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide` - 10 edges
3. `GitHubAPIError` - 8 edges
4. `⚡ GitPulse - GitHub Trending CLI & Web Dashboard` - 8 edges
5. `GitHubRateLimitError` - 5 edges
6. `get_trending()` - 4 edges
7. `main()` - 4 edges
8. `2. Understanding the GitHub API` - 4 edges
9. `Step 5: Hosting on Render` - 4 edges
10. `✨ Features` - 4 edges

## Surprising Connections (you probably didn't know these)
- `get_trending()` --uses--> `GitHubAPIError`  [INFERRED]
  app.py → gh_service.py
- `get_trending()` --calls--> `fetch_trending_repos()`  [EXTRACTED]
  app.py → gh_service.py
- `main()` --calls--> `fetch_trending_repos()`  [EXTRACTED]
  cli.py → gh_service.py

## Import Cycles
- None detected.

## Communities (9 total, 5 thin omitted)

### Community 0 - "🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide"
Cohesion: 0.12
Nodes (15): 1. Create a `Procfile`, 1. Project Overview & Learning Goals, 2. Push Code to GitHub, 3. Deploy on Render, 8. Enhancement Ideas & Practice Challenges, 🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide, Step 1: Environment Setup, Step 2: Shared GitHub API Client (+7 more)

### Community 1 - "⚡ GitPulse - GitHub Trending CLI & Web Dashboard"
Cohesion: 0.15
Nodes (12): 1. Prerequisites, 2. Setup Environment & Dependencies, CLI Help Options:, ☁️ Deployment on Render, ⚡ GitPulse - GitHub Trending CLI & Web Dashboard, 📄 License, 📁 Project Structure, 🚀 Quick Start (+4 more)

### Community 6 - "2. Understanding the GitHub API"
Cohesion: 0.50
Nodes (4): 2. Understanding the GitHub API, Example Request URL:, Query Parameters:, Rate Limits:

### Community 7 - "✨ Features"
Cohesion: 0.50
Nodes (4): 🖥️ 1. Powerful Terminal CLI (`cli.py`), 🌐 2. Interactive Web Dashboard (`app.py` & `templates/index.html`), 🔌 3. Shared Core API Client (`gh_service.py`), ✨ Features

## Knowledge Gaps
- **1 isolated node(s):** `github-trends`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 36 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide` connect `🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide` to `2. Understanding the GitHub API`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **What connects `github-trends` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `🐍 GitHub Trending CLI & Flask Web App - Complete Python Project Guide` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Why does `fetch_trending_repos()` connect `gh_service.py` to `GitHubAPIError`, `app.py`, `cli.py`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Why does `⚡ GitPulse - GitHub Trending CLI & Web Dashboard` connect `⚡ GitPulse - GitHub Trending CLI & Web Dashboard` to `✨ Features`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._