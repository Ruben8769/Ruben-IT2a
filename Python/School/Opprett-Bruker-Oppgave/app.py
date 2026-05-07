import subprocess
import json
from tkinter import filedialog

filnavn = filedialog.askopenfilename()

with open(filnavn, "r") as f:
    users = json.load(f)

for user in users["brukere"]:
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", "create_user.ps1",
        "-givenName", user["navn"],
        "-surname", user["etternavn"],
        "-name", f"{user["navn"]} {user["etternavn"]}",
        "-ou", "OU=Lab-Users"
    ])