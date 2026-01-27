# Importing
import uuid
import firebase_admin
from firebase_admin import credentials, firestore


# Connecting to Firebase
cred = credentials.Certificate("Python/School/Database-Lagerstyring/firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# Making seperate variables
imp_users = db.collection("lager-brukere").get()
imp_storage = db.collection("lager-lager").get()


# Creating functions
def maching_username_password(username_in, password_in):
    for user in imp_users:
        user = user.to_dict()
        if username_in == user["name"]:
            if password_in == user["password"]:
                return True
            return False
    else:
        return False


# Creating user functions
def main():
    user_options = {"1": login}
    while True:
        # Getting user choice
        print("\n--- Start Meny ---\n1) Logg inn\n9) Avslutt\n")
        choice = input("Valg: ")

        # Activating choosen option
        if choice in user_options:
            option = user_options[choice]
            option()
        elif choice == "9":
            break
        else:
            print("\nUgyldig inntastet, prøv på nytt.")


def login():
    print("\n--- Login Meny ---")
    user_name = input("Username: ")
    user_password = input("Password: ")
    if maching_username_password(user_name, user_password):
        print("\nMaching username and password")
        main_menu()
    else:
        print("\nWrong username or password")


def main_menu():
    print("\n--- Main Menu ---")

main()