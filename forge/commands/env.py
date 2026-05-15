import typer
import os
import yaml 
typer = typer.Typer()

# get username from config-forge.yaml
def where_is_env():
	'''
	reading file
	'''
	cwd = os.getcwd()
	with open(cwd + r"\config-forge.yaml") as stream:
		username = yaml.safe_load(stream)['USERNAME']
	
	if os.path.isfile(f"C:/Users/{username}/.env/.env"):
		print(f"Deine env ist in C:/Users/{username}/.env/.env")
	elif os.path.isfile(r"/.env"):
		print("Deine env ist im root dir")
	else:
		# ask if createing this file is okay
		answer = input(f"soll ich die datei in C:/Users/{username}/.env/.env erstellen? : (Y/N) ")
		if (answer == "Y" or answer == "y"):
			with open(f"C:/Users/{username}/.env/.env", "w") as f:
				f.write("Hier kommen deine env Keys rein")
		elif (answer == "N" or answer == "n"):
			print("okay, dann erstelle sie slebst")
		else:
			print("input nicht verstanden")
			return 0
			
		

def run():
	where_is_env()


if __name__ == "__mian__":
	run()
"""
check if .env file is in the current porject or it exists a globaly .env file in ~/.env/.env or will create it and will add a env.py file that to use get.dotenv(xy)
"""
