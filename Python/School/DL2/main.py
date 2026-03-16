# Importering
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import uuid


# Variabler
current_username = None # Navnet til brukeren's login sesjon


# Firebase
cred = credentials.Certificate("Python/School/DL2/firebase_nokel.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Lagrer forskjellige variabler for hvert dokument
def load_firebase():
    global lgs_storage, lgs_user # Gjør variablene globale
    lgs_user = db.collection("lagerstyring-ansatt").get() # Variabel for brukere
    lgs_storage = db.collection("lagerstyring-lager").get() # Variabel for vare lagring

load_firebase() # Laster firebase


# Lager funksjoner
# Funksjon som kjører alt
def main():
    """
    Alle mulige tilstander
    'start' = Startmeny
    'innloget' = Bruker logget inn
    'quit' = Avslutt programet
    """
    current_state = "start"
    while current_state != "quit":
        if current_state == "start":
            current_state = start_menu()
        elif current_state == "innlogget":
            current_state = main_menu()


# Funksjon som laster opp til firebase
def upload_storage(id, amount, low_amount, username, time):
    db.collection("lagerstyring-lager").document(id).set({
        "antall": amount,
        "lav-antall-vare": low_amount,
        "sist-oppdatert": [
            username,
            time
        ],
        "varenr": str(uuid.uuid4()) # Bruker UUID for varenr
    })


# Funksjon som henter localtiden
def localtime():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d") # Bruker - i strtime som jeg får format YYYY-MM-DD


# Startmeny
def start_menu():
    print("\n--- Start Menu ---\n\n  1. Logg inn\n  9. Avslutt\n")
    user_answer = input("Velg: ")
    if user_answer == "1":
        return login()
    elif user_answer == "9":
        return "quit"
    else:
        print("Ugyldig inntastet, prøv på nytt.")


# Bruker 1: admin, q1
# Bruker 2: erl, q1
# Login meny
def login():
    global current_username
    print("\n--- Login ---\n")
    user_name = input("Brukernavn: ")
    user_password = input("Passord: ")
    for user in lgs_user: # Går gjennom hver bruker
        data = user.to_dict() # Gjør gjeldende dokumentet om til dictonary som den er lesebar
        if data["navn"] == user_name and data["passord"] == user_password: # Sjekker om navnet / passordet er det samme som i databasen
            current_username = user_name # Lagrer navn for bruk til framtiden
            return "innlogget" # Går til hovedmenyen hvis innloggingen er korrekt
    else:
        print("\nUgyldig inntastet, prøv på nytt.")
        return "start" # Går tilbake til startmenyen hvis innloggingen er feil


# Hovedmeny
def main_menu():
    print("\n--- Hovedmeny ---\n\n  1. Se produkter\n  2. Modifiser produkt\n  3. Logg-tabell\n")
    user_answer = input("Velg: ")

    if user_answer == "1":
        load_firebase() # Oppdaterer firebase hvis noe nytt er lastet opp fra sist den var oppdatert
        print("\n--- Produkter ---")
        for product in lgs_storage: # Går gjennom hvert dokument
            data = product.to_dict() # Gjør gjeldende dokument til dictonarty
            print(f"""
Navn:       {product.id.title()}
Antall:     {data["antall"]}
Varenumber: {data["varenr"]}""")
            if data["lav-antall-vare"] <= data["antall"]:
                print("Antall Vare Under Grensen!")
    elif user_answer == "2":
        change_product()
    elif user_answer == "3":
        view_log()
    else:
        print("\nUgyldig inntasted, prøv på nytt.")
    return "innlogget"


# Modifiser produkt
def change_product():
    load_firebase()
    print("\n--- Modifiser Produkt ---\n\n  1. Legg til produkt\n  2. Modifiser produkt\n")
    user_answer = input("Velg: ")

    if user_answer == "1":
        add_product()
    elif user_answer == "2":
        modify_product()
    else:
        print("\nUgyldig inntastet, prøv på nytt.")


# Legg til produkt
def add_product():
    print("\n--- Legg Til Produkt ---\n")
    name = input("Navn på vare: ").lower() # Gjør input til små bokstaver
    amount = int(input("Antall av vare: ")) # Gjør input til integer
    low_warning_amount = int(input("Lav vare advarsel: ")) # Gjør input til integer

    for product in lgs_storage:
        if product.id == name:
            print("\nVare allerede i lager.")
            break
    else:
        upload_storage(name, amount, low_warning_amount, current_username, localtime()) # Laster opp til firebase
        print("Vare lastet opp.")
    return "innlogget"

# Modifiser produkt:
def modify_product():
    load_firebase() # Laster firebase på nytt
    # Lager funksjoner, må lage dem før if statment
    def remove_amount(): # Funksjon til og fjerne antall fra vare
        nonlocal final_amount # Bruker nonlocal som at nested funksjonen bruker variablen til hovedfunksjonen
        print("\n--- Fjern Antall ---\n")
        user_remove = int(input("Hvor mange vil du fjerne: "))
        if user_remove > int(data["antall"]): # Hvis antall man vil fjerne er støre enn antall sett til 0
            return 0
        else:
            return int(data["antall"]) - user_remove


    def add_amount(): # Funksjon til og legge til antall fra vare
        nonlocal final_amount
        print("\n--- Legg Til Antall ---\n")
        user_add = int(input("Hvor mange vil du legge til: "))
        return int(data["antall"]) + user_add


    def remove(): # Funksjon for og fjerne vare
        print("\n--- Fjern Vare ---\n")
        user_remove = input("Er du sikker? Ja eller Nei: ").lower()
        if user_remove == "ja":
            db.collection("lagerstyring-lager").document(product.id).delete() # Fjerner dokument
            print("Fjernet vare")


    print("\n--- Modifiser Produkt ---\n")
    user_product = input("Produkt navn: ").lower()
    for product in lgs_storage:
        data = product.to_dict()
        if user_product == product.id.lower():
            final_amount = 0 # Bruker final amount som jeg kan bruke enn annen funksjon til og oppdatere et dokument

            print("\n  1. Fjern antall\n  2. Legg til antall\n  3. Fjern vare\n")
            user_answer = input("Velg: ")

            if user_answer == "1":
                final_amount = remove_amount()
                upload_storage(product.id, final_amount, data["lav-antall-vare"], current_username, localtime()) # Laster opp til firebase
                print("\nFjernet antall")
            elif user_answer == "2":
                final_amount = add_amount()
                upload_storage(product.id, final_amount, data["lav-antall-vare"], current_username, localtime()) # Laster opp til firebase
                print("\nLa til antall")
            elif user_answer == "3":
                remove()
            else:
                print("Ugyldig inntastet, prøv på nytt.")
            break
    else:
        print("\nProdukt ikke funnet.")

    return "innlogget"


# Logg-tabell
def view_log():
    load_firebase()
    print("\n--- Logg Tabel ---\n")
    for product in lgs_storage:
        data = product.to_dict()
        print(f"""
Vare:        {product.id.title()}

Sist Endret: {data["sist-oppdatert"][0]}
             {data["sist-oppdatert"][1]}
""")
    # data["sist-oppdatert"][0] henter første verdi i listen (navn)
    # data["sist-oppdatert"][0] henter andre verdi i listen (når den ble sist oppdatert)
    return "innlogget"

main()