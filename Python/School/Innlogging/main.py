verified_users = [{"username":"admin", "password":"123"}]

def main():
    state = "start"
    while state != "quit":
        if state == "start":
            state = vis_startmeny()
        elif state == "innlogget":
            state = vis_innlogget_meny()

def vis_startmeny():
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
        return "start"

def registrer_bruker_meny():
    print("\n=== Registrer bruker ===\n")
    validusername = False
    validpassword = False
    while validusername == False:
        username = input("Brukernavn: ")
        for user in verified_users:
            if user["username"] == username:
                print("\nBrukernavn allerede i bruk, bruk et annet.\n")
            else:
                validusername = True
                while validpassword == False:
                    password = input("Passord: ")
                    re_password = input("Reskriv passord: ")
                    if password == re_password:
                        new_user = {"username":username, "password":password}
                        verified_users.append(new_user)
                        print("\nNy bruker opprettet ...")
                        validpassword = True
                        return "innlogget"
                    else:
                        print("\nPassorende er ikke like.\n")

def innlogging_meny():
    while True:
        username = input("\nBrukernavn: ")
        password = input("Passord: ")
        for user in verified_users:
            if user["username"] != username or user["password"] != password:
                print("Feil brukernavn eller passord.\n")
            else:
                return "innlogget"

def vis_innlogget_meny():
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

main()