# Ting jeg vil ha med:
# - Lage en ny bruker
# - Lage en ny bruker og legg til i JSON fil
# - Lage ny brukere fra en JSON fil
# - List alle brukere
#
# - Lag ny gruppe
# - List alle grupper

import json
import subprocess

def load_users():
    with open("Python/Tentamen-2IT/users.json", "r") as u:
        return json.load(u)

def add_users_to_json(userdata):
    current_data = load_users()
    current_data.append(userdata)

    with open("Python/Tentamen-2IT/users.json", "w") as u:
        json.dump(current_data, u, indent=4)

def create_user_into_pw():
    print("\n====== Lag Bruker, Rett I PW =======\n")
    in_firstname = input("Fornavn: ")
    in_surname = input("Etternavn: ")
    in_location = input("OU Navn: ")
    in_name = f"{in_firstname} {in_surname}"
    in_samaccountname = f"{in_firstname[0:3].lower()}{in_surname[0:3].lower()}"

    try:
        subprocess.run(
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "Python/Tentamen-2IT/create_user.ps1",
            "-givenName", in_firstname,             # Fornavn
            "-surname", in_surname,                 # Etternavn
            "-name", in_name,                       # Fult Navn
            "-samAccountName", in_samaccountname,   # Login Navn
            "-ou", f"OU={in_location}"              # OU Navn
        )
    except Exception as e:
        print(f"Error, {e}")
    else:
        print("Added user")

def create_user_into_json():
    print("\n====== Lag Bruker, In I JSON =======\n")
    user_data = {}
    in_firstname = input("Fornavn: ")
    in_surname = input("Etternavn: ")
    user_data = {
        "fornavn":in_firstname,
        "etternavn":in_surname,
        "name":f"{in_firstname} {in_surname}",
        "samaccountname":f"{in_firstname[0:3].lower()}{in_surname[0:3].lower()}"
    }

    try:
        add_users_to_json(user_data)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("\nLa bruker til JSON fil")

def add_user_from_json():
    print("\n====== Lag brukere fra JSON fil =======\n")
    try:
        users = load_users()
        in_location = input("OU Navn: ")
        for user in users:
            subprocess.run(
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "Python/Tentamen-2IT/create_user.ps1",
            "-givenName", user["fornavn"],              # Fornavn
            "-surname", user["etternavn"],              # Etternavn
            "-name", user["name"],                      # Fult Navn
            "-samAccountName", user["samaccountname"],  # Login Navn
            "-ou", f"OU={in_location}"                  # OU Navn
        )
    except Exception as e:
        print(f"Error {e}")
    else:
        print("La til brukere")

def list_all_users():
    print("\n====== Print Alle Brukere ======\n\n--- Brukere I JSON ---\n")
    try:
        users = load_users()
        for user in users:
            print(f"  Navn            :  {user["name"]}\n  SamAccountName  :  {user["samaccountname"]}\n")
        
        print("--- Brukere I Domene ---\n")
        result = subprocess.run([
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "Python/Tentamen-2IT/create_user.ps1"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error {e}")

def create_group():
    print("\n======= Lag Gruppe ======\n")
    in_name = input("Navn: ")
    in_samaccountname = input("SamAccountName: ")
    in_location = input("OU Navn:")
    try:
        subprocess.run(
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "Python/Tentamen-2IT/create_group.ps1",
            "-Name", in_name,
            "-SamAccountName", in_samaccountname,
            "-ou", f"OU={in_location}"
        )
    except Exception as e:
        print(f"Error {e}")
    else:
        print("\nLaget ny gruppe")

def list_all_groups():
    print("\n====== Print Alle Grupper =======")
    try:
        result = subprocess.run([
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "Python/Tentamen-2IT/create_user.ps1"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error {e}")

# Main loop
running = True
while running:
    print("""
====== Start Meny ======

    1. Lag bruker
    2. Lag bruker og legg i JSON fil
    3. Leg til brukere fra JSON fil
    4. List alle brukere (Inkludert JSON filen)
    5. Lag ny gruppe
    6. List alle grupper
""")
    choice = input("Velg: ")
    if choice == "1":
        create_user_into_pw()
    elif choice == "2":
        create_user_into_json()
    elif choice == "3":
        add_user_from_json()
    elif choice == "4":
        list_all_users()
    elif choice == "6":
        list_all_groups()