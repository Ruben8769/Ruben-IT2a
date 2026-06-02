import json
import os

ACTIVE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_json():
    file_path = os.path.join(ACTIVE_DIR, "ad_brukere_50.json")
    with open(file_path, "r") as f:
        return json.load(f)

# Mobilnummeret til Nora Aas
def mbna():
    data = get_json()
    for user in data:
        if user["displayName"] == "Nora Aas":
            print(f"\nNora Aas telefonummer {user["mobile"]}\n")

mbna()

# Avdelning Alexander  Aune
def ahb():
    data = get_json()
    for user in data:
        if user["displayName"] == "Alexander Aune":
            print(f"\nAlexander department {user["department"]}\n")

ahb()

# E-posten Frida Berge
def ees():
    data = get_json()
    for user in data:
        if user["displayName"] == "Frida Berge":
            print(f"\nFrida Berge {user["mail"]}\n")

ees()

# Grupper aurora.rusten
def goj():
    data = get_json()
    for user in data:
        if user["sAMAccountName"] == "aurora.rusten":
            print("\naurora.rusten")
            for member in user["memberOf"]:
                print(member)
            print("")

goj()

# Ansattnummer A1027
def aa():
    data = get_json()
    for user in data:
        if user["employeeID"] == "A1027":
            print(f"\nA1027 {user["displayName"]}\n")

aa()

# Brukere disabled
def bd():
    data = get_json()
    count = 0
    for user in data:
        if user["accountEnabled"] == False:
            count += 1
    print(f"\nCount {count}\n")

bd()

# IT-Depratment
def itd():
    data = get_json()
    count = 0
    for user in data:
        if user["depratment"] == "IT":
            count += 1
    print(f"\nIn IT-Depratment {count}\n")

# Logget inn sist
def lis():
    data = get_json()
    for user in data:
        pass

lis()

# Medlem av gruppe GG_Ansatte
def mggga():
    data = get_json()
    count = 0
    for user in data:
        if "GG_Ansatte" in user["memberOf"]:
            count += 1
    print(f"\nMedlem {count}\n")

mggga()

# Fult navn og OU
def fno():
    data = get_json()
    count = 0
    for user in data:
        if user["manager"] == "CN=Rektor Nesna,OU=Ledelse,OU=Ansatte,DC=nesna,DC=local":
            print(f"\nFult navn {user["displayName"]} Stilling {user["department"]}\n")

fno()

# Endre Nora Aas Tlf
def enat():
    data = get_json()
    file_path = os.path.join(ACTIVE_DIR, "ad_brukere_50.json")
    for user in data:
        if user["displayName"] == "Nora Aas":
            user["mobile"] = "+47 99991122"
            user["telephoneNumber"] = "+47 99 99 11 22"
            new_data = data
            print(user["mobile"])
            print(user["telephoneNumber"])
            print(new_data)
            # with open(file_path, "w") as f:
            #     json.dump(new_data, f, indent=4)

enat()