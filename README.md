# forge ist eine lib um schneller dinge wie den setup zu machen

einfach installieren als cli tool und dann los geht.
schreibe `forge --help` um alle verfügbaren befehle zu sehen.

# existierende befehle

`forge --help`
zeigt im terminal an welche befehle es gibt 

`forge startup`
erstellt eine config-forge.yaml file in der die dinge wie username, projectname ** abgefragt werden und diese sollten berfüllt werden, sonst passieren fehler

`forge env`
zeigt dir wo die env datei liegt wenn die existiert, wenn nicht dann wird die env unter "C:\users\{username}\.env\.env" erstellt

`forge requrements`
schaut in allen python daten nach was importiert wurde und erstellt eine requrements-dev.txt file mit allen reqirements die installiert wurden