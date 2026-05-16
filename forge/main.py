import typer
from rich.console import Console
from .commands.env import run
from .commands.startup import startup_run
from .commands.requirements import create_requirements_file
from .commands.db import testcpnnection



app = typer.Typer()
console = Console()


'''
if the startup.py command didn´t run 1 time, dont run any commands. this works if the file config.yaml dosnt exists, do not run any commands again 
'''

@app.command()
def startup():
	startup_run()


@app.command()
def env():
	run()

@app.command()
def requirements():
	create_requirements_file()

@app.command()
def testcon():
	testcpnnection()

if __name__ == "__main__":
    app()