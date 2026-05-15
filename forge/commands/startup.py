import typer
import os
import yaml
typer = typer.Typer()

def startup():
	cwd = os.getcwd()
	if os.path.isfile(cwd+"config-forge.yaml"):
		print("datei existiert schon")
	else:
		with open(cwd + r"\config-forge.yaml", "x",) as f:
			f.write("USERNAME: \nPROJECTNAME: ")
			

def startup_run():
	startup()

if __name__ == "__main__":
	startup_run()
'''
this creates a config-forge.yaml where is asked for username and later for every other thing
'''