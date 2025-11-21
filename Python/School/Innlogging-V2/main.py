# Importering
import backend as be
import time

# Variabler

# Funksjoner
def main():
    """
        Alle forskjellige tilstander:
        "start" - Startmeny
        "innlogget" - Innloggings meny
        "quit" - Avslutt
    """
    current_state = "start"
    while current_state != "quit":
        if current_state == "start":
            current_state = startmeny()
        elif current_state == "innlogget":
            current_state = hovedmeny()

def startmeny():
    print("\n=== STARTMENY ===\n1) Logg inn\n2) Registrer bruker\n3) Avslutt\n")
    user_choice = input("Hva ønsker du og gjøre: ")
    if user_choice == "1":
        return innlogging_meny()
    elif user_choice == "2":
        return registrer_bruker_meny()
    elif user_choice == "3":
        return "quit"
    else:
        print("Ugyldig svar, skriv igjen.")
        return "start"

def registrer_bruker_meny():
    print("\n=== Registrer bruker ===\n")
    while True:
        username = input("Brukernavn: ")
        password = input("Passord: ")
        re_password = input("Reskriv passord: ")
        if password != re_password:
            print("Passordene er ikke like!")
        elif len(username) and len(password):
            if be.legal_str(password) and be.legal_str(username):
                if not be.matching_usr(username):
                    be.dump_data(username, password)
                    print("Logger deg in")
                    loading_animation(3)
                    return "innlogget"
                else:
                    print("\nBrukernavn tatt\n")
            else:
                print("\nUgyldig brukernavn eller passord!\n")
        else:
            print("\nUgyldig brukernavn eller passord!\n")

def innlogging_meny():
    print("\n=== Logg in ===\n")
    while True:
        username = input("Brukernavn: ")
        password = input("Passord: ")
        if len(username) and len(password):
            if be.legal_str(password) and be.legal_str(username):
                if be.matching_usr_psw(username, be.encryption(password)):
                    print("Logger deg in")
                    loading_animation(2)
                    return "innlogget"
                else:
                    print("\nUgyldig brukernavn eller passord\n")
            else:
                print("\nUgyldig brukernavn eller passord!\n")
        else:
            print("\nUgyldig brukernavn eller passord!\n")

def hovedmeny():
    print("\n=== MENY ===\n1) Logg ut\n3) Avslutt\n")
    user_choice = input("Hva ønsker du og gjøre: ")
    if user_choice == "1":
        print("Logger deg ut")
        loading_animation(2)
        return "start"
    elif user_choice == "3":
        return "quit"

def loading_animation(tim):
    doth = "."
    for x in range(tim):
        print(doth)
        doth = doth + "."
        time.sleep(.3)

main()