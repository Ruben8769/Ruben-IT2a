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
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))




# JSON Handling


def load_users():
    script_file = os.path.join(SCRIPT_DIR, "users.json")
    with open(script_file, "r") as u:
        return json.load(u)


def add_users_to_json(userdata):
    script_file = os.path.join(SCRIPT_DIR, "users.json")
    current_data = load_users()
    current_data.append(userdata)

    with open(script_file, "w") as u:
        json.dump(current_data, u, indent=4)


def remove_users_json(sam_account_name):
    script_file = os.path.join(SCRIPT_DIR, "users.json")

    current_data = load_users()
    original_count = len(current_data)
    
    updated_data = [user for user in current_data if user["samaccountname"] != sam_account_name]
    
    if len(updated_data) < original_count:
        with open("Python/Tentamen-2IT/users.json", "w") as u:
            json.dump(updated_data, u, indent=4)
        print(f"Bruker '{sam_account_name}' ble fjernet.")
    else:
        print(f"Fant ingen bruker med samAccountName '{sam_account_name}'.")




#   Seksjon: Lag


def create_user_cm(firstname, surname, name, samaccountname, location):
    script_file = os.path.join(SCRIPT_DIR, "create_user.ps1")
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", script_file,
        "-givenName", firstname,
        "-surname", surname,
        "-name", name,
        "-samAccountName", samaccountname,
        "-ou", f"OU={location}"
    ])
    # def cm(link):
    #     subprocess.run([
    #         "powershell",
    #         "-ExecutionPolicy", "Bypass",
    #         "-File", link,
    #         "-givenName", firstname,
    #         "-surname", surname,
    #         "-name", name,
    #         "-samAccountName", samaccountname,
    #         "-ou", f"OU={location}"
    #     ])
    # try:
    #     cm("Python/Tentamen-2IT/create_user.ps1")
    # except:
    #     print("\nPrøvde normal link, gikk ikke. Prøver kortere link\n")
    #     try:
    #         cm("create_user.ps1")
    #     except Exception as e:
    #         print(f"Bruker ikke lagret. Error {e}")
    #     else:
    #         print("Bruker laget")
    # else:
    #     print("Bruker laget")


def create_group_cm(name, samaccountname, location):
    script_file = os.path.join(SCRIPT_DIR, "create_group.ps1")
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", script_file,
        "-Name", name,
        "-SamAccountName", samaccountname,
        "-ou", f"OU={location}"
    ])
    # def cm(link):
    #     subprocess.run([
    #         "powershell",
    #         "-ExecutionPolicy", "Bypass",
    #         "-File", link,
    #         "-Name", name,
    #         "-SamAccountName", samaccountname,
    #         "-ou", f"OU={location}"
    #     ])
    # try:
    #     cm("Python/Tentamen-2IT/create_group.ps1")
    # except:
    #     print("\nPrøvde normal link, gikk ikke. Prøver kortere link\n")
    #     try:
    #         cm("create_group.ps1")
    #     except Exception as e:
    #         print(f"Bruker ikke lagret. Error {e}")
    #     else:
    #         print("Bruker laget")
    # else:
    #     print("Bruker laget")


def create_user_into_pw():
    print("\n====== Lag Bruker, Rett I PW =======\n")
    in_firstname = input("Fornavn: ")
    in_surname = input("Etternavn: ")
    in_location = input("OU Navn: ")
    in_name = f"{in_firstname} {in_surname}"
    in_samaccountname = f"{in_firstname[0:3].lower()}{in_surname[0:3].lower()}"
    try:
        create_user_cm(in_firstname, in_surname, in_name, in_samaccountname, in_location)
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
        "navn":f"{in_firstname} {in_surname}",
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
            create_user_cm(user["fornavn"], user["etternavn"], user["navn"], user["samaccountname"], in_location)
    except Exception as e:
        print(f"Error {e}")
    else:
        print("La til brukere")


def create_group():
    print("\n======= Lag Gruppe ======\n")
    in_name = input("Navn: ")
    in_samaccountname = input("SamAccountName: ")
    in_location = input("OU Navn:")

    try:
        create_group_cm(in_name, in_samaccountname, in_location)
    except Exception as e:
        print(f"Error {e}")
    else:
        print("\nLaget ny gruppe")




#   Seksjon: Print Ut


def list_users_groups_cm(mode):
    script_file_user = os.path.join(SCRIPT_DIR, "list_user.ps1")
    script_file_group = os.path.join(SCRIPT_DIR, "list_group.ps1")
    if mode == 1:
        return subprocess.run([
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", script_file_user],
            capture_output=True,
            text=True
        )
    if mode == 2:
        return subprocess.run([
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", script_file_group],
            capture_output=True,
            text=True
        )
    # def cm_user(link):
    #     return subprocess.run([
    #         "powershell",
    #         "-ExecutionPolicy", "Bypass",
    #         "-File", link],
    #         capture_output=True,
    #         text=True
    #     )
    # def cm_group(link):
    #     return subprocess.run([
    #         "powershell",
    #         "-ExecutionPolicy", "Bypass",
    #         "-File", link],
    #         capture_output=True,
    #         text=True
    #     )
    # if mode == 1:
    #     try:
    #         cm_user("Python/Tentamen-2IT/list_user.ps1")
    #     except:
    #         print("\nPrøvde normal link, gikk ikke. Prøver kortere link\n")
    #         try:
    #             cm_user("list_user.ps1")
    #         except Exception as e:
    #             print(f"Error {e}")
    # elif mode == 2:
    #     try:
    #         cm_group("Python/Tentamen-2IT/list_group.ps1")
    #     except:
    #         print("\nPrøvde normal link, gikk ikke. Prøver kortere link\n")
    #         try:
    #             cm_group("list_group.ps1")
    #         except Exception as e:
    #             print(f"Error {e}")


def list_all_users_json():
    print("\n====== Print Alle Brukere (JSON) ======\n\n")
    try:
        users = load_users()
        for user in users:
            print(f"  Navn            :  {user["navn"]}\n  SamAccountName  :  {user["samaccountname"]}\n")
    except Exception as e:
        print(f"Error {e}")


def list_all_users_domain():
    print("\n====== Print Alle Brukere (Domene) ======\n")
    try:
        users = list_users_groups_cm(1)
        print(users.stdout)
    except Exception as e:
        print(f"Error {e}")


def list_all_groups():
    print("\n====== Print Alle Grupper =======")
    try:
        list_users_groups_cm(2)
    except Exception as e:
        print(f"Error {e}")




#   Sekjson: Fjern


def remove_user(mode):
    if mode == 1:
        print("\n====== Fjern Bruker (Fra JSON File) ======\n")
        sam_account_name = input("SamAccountName: ")
        try:
            remove_users_json(sam_account_name)
        except Exception as e:
            print(f"Error {e}")
    elif mode == 2:
        pass




# Hovedløkke
running = True
while running:
    print("""
====== Start Meny ======

--- Lag ---
    a1. Lag bruker
    a2. Lag bruker og legg i JSON fil
    a3. Lag brukere fra JSON fil
    a4. Lag ny gruppe

--- List ---
    b1. List alle brukere fra JSON fil
    b2. List alle brukere fra Domenen
    b3. List alle grupper

--- Fjern ---
    c1. Fjern bruker fra JSON
    c2. Fjern bruker fra domene
    c3. Fjern gruppe

--- OU ---
    d1. List OU-er
    d2. Ny OU
    d3. Modifiser OU
    d4. Fjern OU
""")
    choice = input("Velg: ")
    if choice == "a1":
        create_user_into_pw()
    elif choice == "a2":
        create_user_into_json()
    elif choice == "a3":
        add_user_from_json()
    elif choice == "a4":
        create_group()

    elif choice == "b1":
        list_all_users_json()
    elif choice == "b2":
        list_all_users_domain()
    elif choice == "b3":
        list_all_groups()
    
    elif choice == "c1":
        remove_users_json()
    elif choice == "c2":
        pass
    elif choice == "c3":
        pass