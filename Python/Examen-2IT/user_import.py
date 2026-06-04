# Importering
import os
import json
import subprocess

# Henter fil linker
ACTIVE_DIR = os.path.dirname(os.path.abspath(__file__)) # Får Active Directory som koden kjører i
JSON_FILE = os.path.join(ACTIVE_DIR, "polar_ansatte.json") # Kombinerer AD med local fil lokasjon
NEW_USER = os.path.join(ACTIVE_DIR, "newUser.ps1") # Kombinerer AD med local fil lokasjon
ADD_USER_TO_GROUP = os.path.join(ACTIVE_DIR, "userToGroup.ps1")

# Funksjon for og få JSON data
def call_json_list():
    with open(JSON_FILE, "r", encoding="utf-8") as data:
        return json.load(data)

# Funksjon for og lage brukere
def create_user(firstname, surname, username, ou, email, phonenummber, jobtitle, department): # Bruker inputs i funksjonen for og hente data
    subprocess.run([ # Kjører PowerShell script
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", NEW_USER,
        "-firstname", firstname,
        "-surname", surname,
        "-username", username,
        "-ou", ou,
        "-email", email,
        "-phonenummber", phonenummber,
        "-jobtitle", jobtitle,
        "-department", department
    ])

# Funksjon for og legge bruker in i gruppe
def add_user_to_group(userPrincipalName, indentity):
    subprocess.run([ # Kjører PowerShell script
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", ADD_USER_TO_GROUP,
        "-userPrincipalName", userPrincipalName,
        "-indentity", indentity
    ])

# Test funksjon for og liste alle brukere
def list_users():
    data = call_json_list() # Henter JSON data
    for user in data["ansatte"]:
        print(user["etternavn"])
# list_users()

# Funksjon som går gjennom ver bruker og legger de til i AD
def add_users():
    data = call_json_list() # Henter JSON data
    for user in data["ansatte"]:
        split_username = user["brukernavn"].split(".") # Spliter et string på til to (i en liste)
        completed_username = f"{split_username[0][0:3]}{split_username[1][0:3]}" # Bruker de tre første bokstavene i fornavnet og etternavnet

        # Finner ut hvor den ansatte er
        ouPath = "Null"
        if user["lokasjon"] == "Nesna":
            ouPath = "OU=Nesna,OU=PES,DC=polar,DC=local"
        else:
            ouPath = "OU=Bodo,OU=PES,DC=polar,DC=local"
        print(ouPath)
        # Kaller på funksjon som legger til bruker i AD
        fornavn = user["fornavn"]
        etternavn = user["etternavn"]
        epost = user["epost"]
        telefon = user["telefon"]
        stilling = user["stilling"]
        avdeling = user["avdeling"]
        create_user(fornavn, etternavn, completed_username, ouPath, epost, telefon, stilling, avdeling)
        gruppe = user["gruppe"]
        add_user_to_group(completed_username, gruppe)

# En løke som kjører koden
while True:
    print("Skriv brukere i AD y eller n: ")
    choice = input("Velg: ")
    if choice == "y":
        print("Legger til brukere")
        add_users()
    else:
        print("Legger ikke brukere i AD")