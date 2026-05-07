import json
import subprocess

with open("Python/School/Opprett-Bruker-Oppgave/users.json", "r") as f:
    users = json.load(f)

for user in users:
    subprocess.run(
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", "Python/School/Opprett-Bruker-Oppgave/create_user.ps1",
        "-givenName", user["fornavn"],
        "-surname", user["etternavn"],
        "-name", f"{user["fornavn"]} {user["etternavn"]}",
        "-samAccountName", f"{user["fornavn"][0:4]}{user["etternavn"][0:4]}"
        "-ou", "OU=Automation"
    )