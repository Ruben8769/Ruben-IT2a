import json
print("JSON imported")
import os
print("OS imported")

ACTIVE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DATA = os.path.join(ACTIVE_DIR, "polar_ansatte.json")
print("Files Loaded")

# JSON Data
def get_json_fixed():
    with open(JSON_DATA, "r", encoding="utf-8") as data:
        return json.load(data)

def get_json():
    with open(JSON_DATA, "r", encoding="utf-8") as data:
        userdata = json.load(data)
        return userdata["ansatte"]


def legg_til_brukere_json(userdata):
    current_data = get_json_fixed()
    current_data["ansatte"].append(userdata)

    with open(JSON_DATA, "w", encoding="utf-8") as data:
        json.dump(current_data, data, indent=4)

def oppdater_json(userdata):
    with open(JSON_DATA, "w", encoding="utf-8") as data:
        json.dump(userdata, data, indent=4)

# Funksjoner
def vis_meny():
    print("\n=== Brukeradministrasjon ===")
    print("1. Vis alle brukere")
    print("2. Legg til bruker")
    print("3. Slett bruker")
    print("4. Endre e-post")
    print("5. Avslutt")


def vis_brukere():
    print("\n--- Alle brukere ---")

    # List ut alle brukere
    data = get_json()
    for user in data:
        print(f"""
    {user["fornavn"]} {user["etternavn"]}
    {user["epost"]}
    Avdeling : {user["avdeling"]}
    Stilling : {user["stilling"]}
""")


def legg_til_bruker():
    print("\n--- Legg til bruker ---")

    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn: ")
    brukernavn = input("Brukernavn: ")
    stilling = input("Stilling: ")
    avdeling = input("Avdeling: ")
    epost = input("Epost: ")
    gruppe = input("Gruppe (GG_Nesna, GG_Bodo, GG_Direktor): ")

    ny_bruker = {
        "fornavn": fornavn,
        "etternavn": etternavn,
        "brukernavn": brukernavn,
        "stilling": stilling,
        "avdeling": avdeling,
        "epost": epost,
        "gruppe": gruppe
    }

    # Legg brukeren inn i listen
    legg_til_brukere_json(ny_bruker)
    print("Bruker lagt til")


def slett_bruker():
    print("\n--- Slett bruker ---")

    brukernavn = input("Brukernavn som skal slettes: ")

    # Finn brukeren og slett den fra listen
    ny_data = []
    data = get_json()
    for user in data:
        if user["brukernavn"] != brukernavn:
            ny_data.append(user)
    data = ny_data
    legg_til_brukere_json(ny_data)


def endre_epost():
    print("\n--- Endre e-post ---")
    data = get_json_fixed()
    brukernavn = input("Fornavn: ")
    for user in data["ansatte"]:
        if user["fornavn"] == brukernavn:
            ny_epost = input("Ny e-post: ")
            user["epost"] = ny_epost
            bruker_funnet = True
            break
            # oppdatert_bruker = {
            #     "fornavn": user["fornavn"],
            #     "etternavn": user["etternavn"],
            #     "brukernavn": user["brukernavn"],
            #     "stilling": user["stilling"],
            #     "avdeling": user["avdeling"],
            #     "epost": ny_epost,
            #     "gruppe": user["gruppe"]
            # }
            # legg_til_brukere_json(oppdatert_bruker)
    if bruker_funnet:
        oppdater_json(data)
        print("E-post oppdatert")
    else:
        print("Fant ikke brukeren")


while True:
    vis_meny()

    valg = input("Velg et alternativ: ")

    if valg == "1":
        vis_brukere()
    elif valg == "2":
        legg_til_bruker()
    elif valg == "3":
        slett_bruker()
    elif valg == "4":
        endre_epost()
    elif valg == "5":
        print("Avslutter programmet.")
        break
    else:
        print("Ugyldig valg.")