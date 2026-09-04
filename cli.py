import typer
from rich.console import Console
from rich.table import Table

from gh_service import fetch_trending_repos

app = typer.Typer(help="CLI tool for fetching trending GitHub repositories")
console = Console()

@app.command()
def main(
    duration: str = typer.Option("weekly", help="Duration for trending repositories (daily, weekly, monthly, yearly)"),
    limit: int = typer.Option(10, help="Number of repositories to fetch"),
    language: str = typer.Option("", help="Programming language filter"),
):
    if duration.lower() not in ["daily", "weekly", "monthly", "yearly"]:
        console.print("[red]Invalid duration. Please choose from daily, weekly, monthly, yearly.[/red]")
        raise typer.Exit(code=1)

    if limit <= 0:
        console.print("[red]Invalid limit. Please provide a positive number.[/red]")
        raise typer.Exit(code=1)
    lang_str = f" in [cyan]{language}[/cyan]" if language else ""

    console.print(f"\nFetching [green]{limit}[/green] trending repositories for [yellow]{duration}[/yellow]{lang_str}...\n")

    try:
        repos = fetch_trending_repos(duration=duration, limit=limit, language=language)

        if not repos:
            console.print("[yellow]No trending repositories found.[/yellow]")
            raise typer.Exit()

        table = Table(title=f"Trending GitHub Repositories {duration.capitalize()}", show_lines=True)
        table.add_column("Rank", style="bold cyan", justify="center", width=6)
        table.add_column("Repository", style="bold white")
        table.add_column("Language", style="magenta", width=14)
        table.add_column("Stars ⭐", style="yellow", justify="right", width=12)
        table.add_column("Forks 🍴", style="green", justify="right", width=12)

        for i, repo in enumerate(repos, start=1):
            fullname = repo.get("full_name")
            desc = repo.get("description", "")
            url = repo.get("html_url", "")
            repo_info = f"[bold blue]{fullname}[/bold blue]\n{desc}\n[url={url}]{url}[/url]"

            table.add_row(
                str(i),
                repo_info,
                repo.get("language", "N/A"),
                str(repo.get("stargazers_count", 0)),
                str(repo.get("forks_count", 0))
            )

        console.print(table)
        console.print(f"\n[dim]Showing {len(repos)} trending repositories[/dim]\n")

    except Exception as e:
        console.print(f"[red]Error fetching trending repositories: {e}[/red]\n")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
