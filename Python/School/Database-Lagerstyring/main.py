# Importing
import uuid
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

print("Imports done")

# Creating Variables
current_user_id = None
product_id = None

print("Variables done")

try:
    # Connecting to Firebase
    cred = credentials.Certificate("Python/School/Database-Lagerstyring/firebase_nokel.json")
    print("Certificate loaded")
    
    firebase_admin.initialize_app(cred)
    print("Firebase initilazed")

    db = firestore.client()
    print("Firebase store created")

    # Making seperate variables for each collection
    lgs_user = db.collection("lagerstyring-ansatt").get()
    print("User fetched")
    lgs_storage = db.collection("lagerstyring-lager").get()
    print("Storage fetched")
except Exception as e:
    print("Error", e)


# Creating functions
# Main function to loop everything
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


# Function for startmenu
def start_menu():
    print("\n--- Start Menu ---\n\n1. Logg inn\n9. Avslutt\n")
    user_answer = input("Velg: ")
    if user_answer == "1":
        return login()
    elif user_answer == "9":
        return "quit"
    else:
        print("Ugyldig inntastet, prøv på nytt.")


# Function for login
def login():
    global current_user_id
    print("\n--- Login ---\n")
    user_name = input("Brukernavn: ")
    user_password = input("Passord: ")
    for user in lgs_user:
        lgs_data = user.to_dict()
        if lgs_data["navn"] == user_name and lgs_data["passord"] == user_password:
            current_user_id = user.id # Lagrer ID for bruk til framtiden
            return "innlogget"
    else:
        print("Ugyldig inntastet, prøv på nytt.")
        return "start"


# Function for main menu
def main_menu():
    print("\n--- Main Menu ---\n\n  1. Se produkter\n  2. Modifiser  produkt\n  3. Logg-tabell\n")
    user_answer = input("Velg: ")

    if user_answer == "1":
        return view_products(1, False)
    elif user_answer == "2":
        return change_product()
    elif user_answer == "3":
        return view_logg()
    else: "Ugyldig inntasted, prøv på nytt"


# Function for viewing products
def view_products(mode, product_name):
    global product_id

    if mode == 1 or mode == 2: 
        for product in lgs_storage:
            print("\n--- Se Produkter ---")
            data = product.to_dict()
            print(f"""
    Vare:        {product.id}
    Vare antall: {data["antall"]}
    Vare nr:     {data["varenr"]}""")
    elif mode == 3:
        for product in lgs_storage:
            if product.id.lower() == product_name.lower():
                product_id == product_name
    else:
        print(product_name, product.id)
        product_id = None
        
    """
    Forskjelige modes
    1 = Skal ta deg tilbake til hovedmenyen
    2 = Skal ikke ta deg tilbake til hovedemyen
    3 = Skal returnere produkt ID hvis den fins
    """
    if mode == 1:
        return "innlogget"
    elif mode == 2 or 3:
        pass
    else:
        return ("innlogget")


# Function for changing amount
def change_product():
    global product_id
    view_products(2, False)
    print("\n--- Modifiser produkt ---\n\n  1. Rediger produkt\n")
    user_answer = input("Velg: ")

    if user_answer == "1":
        user_product = input("\nHvilket produkt vi du endre: ")
        found_product = view_products(3, user_product)

        if product_id == None:
            print("Ingen produkt funnet.")
        else:
            print("Produkt funnet", product_id, user_product)
    else:
        pass
    #     return "innlogget"
    # return "innlogget"


# Function for viewing logg
def view_logg():
    return "innlogget"

main()
