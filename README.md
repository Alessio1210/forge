# forge ist eine lib um schneller dinge wie den setup zu machen

einfach installieren als cli tool und dann los geht.
schreibe `forge --help` um alle verfügbaren befehle zu sehen.

# installieren
wenn du `forge` als cli tool überall auf deinem pc benutzen willst, installiere es am besten mit `pipx`:
```
git clone https://github.com/Alessio1210/forge
cd forge

# pipx installieren, falls du es noch nicht hast
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# terminal neu starten, dann forge installieren
pipx install -e .
```

danach kannst du `forge` in jedem ordner im terminal benutzen:
```
forge --help
```


# existierende befehle

`forge --help`
zeigt im terminal an welche befehle es gibt 

`forge startup`
erstellt eine config-forge.yaml file in der die dinge wie username, projectname ** abgefragt werden und diese sollten berfüllt werden, sonst passieren fehler

`forge env`
zeigt dir wo die env datei liegt wenn die existiert, wenn nicht dann wird die env unter "C:\users\{username}\.env\.env" erstellt

`forge requrements`
schaut in allen python daten nach was importiert wurde und erstellt eine requrements-dev.txt file mit allen reqirements die installiert wurden

`forge testcon`
frage dich ein paar dinge und wenn du diese richtig beantwortet hast, wird einfach eine kurze connection getestet und damit kannst du testen ob die verbindung gelappt hat oder nicht funkitoniert
