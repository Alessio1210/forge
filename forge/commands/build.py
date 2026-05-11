import pandas as pd
import typer

app = typer.Typer()


@app.command()
def build():
    pass


@app.command()
def get_build_information():
    pass


"""
build CI/CD pipeline
build project -> frontende framework -> backend -> temnplate git repo
build route endpoint for APIs in API folder in backend -> creates preview for what will be written and will then create for programming language x a file named routes.forge.dev.xx
"""
