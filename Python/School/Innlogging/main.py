import time
import json

def main():
    current_state = "start"
    while current_state != "quit":
        if current_state == "start":
            current_state = startmeny()
        elif current_state == "innlogget":
            current_state = hovedmeny()

def startmeny():
    print("""
=== STARTMENY ===
1) Logg inn
2) Registrer ny bruker
3) Avslutt
""")
    valg = input("Hva ønsker du og gjøre? ")
    if valg == "1":
        return innlogging_meny()
    elif valg == "2":
        return registrer_bruker_meny()
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig svar, prøv igjen.")
        return("start")

def registrer_bruker_meny():
    print("\n=== Registrer bruker ===\n")
    # Importerer bruker data
    with open("Python/School/Innlogging/brukere.json", "r") as u:
        verified_users = json.load(u)
    # Username creation
    validusername = False
    username_taken = True
    while validusername == False:
        username = input("Brukernavn: ")
        if len(verified_users) != 0:
            for user in verified_users:
                if user["username"] != username:
                    username_taken = False
                elif user["username"] == username:
                    username_taken = True
                    break
            if username_taken:
                print("Brukernavnet er tatt, velg et annet.")
            else:
                username_taken = False
                validusername = True
        else:
            username_taken = False
            validusername = True
    # Password creation
    validpassword = False
    while validpassword == False:
        password = input("Passord: ")
        re_password = input("Reskriv passord: ")
        if password == re_password:
            new_user = {"username":username, "password":password}
            verified_users.append(new_user)
            with open("Python/School/Innlogging/brukere.json", "w") as u:
                json.dump(verified_users, u, indent=4)
            # Bruker login lasting
            print("\nNy bruker opprettet.")
            loading()
            validpassword = True
            return "innlogget"
        else:
            print("\nPassorende er ikke like.\n")

def innlogging_meny():
    print("\n=== Registrer bruker ===\n")
    # Importerer bruker data
    with open("Python/School/Innlogging/brukere.json", "r") as u:
        verified_users = json.load(u)
    # Reigstrerer bruker
    if len(verified_users) != 0:
        print("\n=== Logg in ===\n")
        loggin_state = True
        while loggin_state:
            username = input("Brukernavn: ")
            password = input("Passord: ")
            for user in verified_users:
                if user["username"] == username and user["password"] == password:
                    loading()
                    loggin_state = False
                    return "innlogget"
            print("Feil brukernavn eller passord.\n")
    else:
        print("\nNo users availible.")
        return "start"

def hovedmeny():
    print("""
=== MENY (innlogget) ===
1) Fortell en random vits
2) Logg ut
3) Avslutt
""")
    valg = input("Hva ønsker du å gjøre? ")
    if valg == "1":
        return "innlogget"
    elif valg == "2":
        print("Du er nå logget ut.")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
        return "innlogget"

def loading():
    print("\nLogger bruker inn")
    doth = "."
    for x in range(3):
        print(doth)
        doth = doth + "."
        time.sleep(.3)

main()