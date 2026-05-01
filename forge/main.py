import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def main():
    print("test")

