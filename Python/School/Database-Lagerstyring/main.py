# Importing
import backend

# Creating functions
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
    print("\n--- Login Meny ---\n")
    user_name = input("Username: ")
    user_password = input("Password: ")




main()