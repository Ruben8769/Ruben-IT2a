import time

loggedInn = False
users = [] #{"username": Ole, "password": 123456}
jokes = [
    "Hva sa den ene tørrfisken til den andre? Long time no sea",
    "Hvilket tre er datamaskinens favoritt tre? 100110100110",
    "Hva sa den nærsynte til den langsynte? Hører du hva jeg sier?"
]

def login():
    global loggedInn
    user_name = input("Brukernavn: ")
    password = input("Password: ")
    for user in users:
        if user["username"] == user_name and user["password"] == password:
            loggedInn = True
            break
    if not loggedInn:
        print("Feil brukernavn eller passord...")
    else:
        print(f"Logger {user_name} inn")
        print(".")
        time.sleep(.2)
        print("..")
        time.sleep(.2)
        print("...")
        time.sleep(.2)
        print("....")
        time.sleep(.2)
        print(".....")
        time.sleep(.5)
        print("Du er logget inn")

def create_user():
    user_name = ""
    while len(user_name) == 0:
        user_name = input("Brukernavn: ")
        for user in users:
            if user["username"] == user_name:
                print("Velg et annet brukernavn")
                user_name = ""

    while True:
        password = input("Password: ")
        re_password = input("Rewrite password: ")
        if password == re_password:
            new_user = {"username": user_name, "password": password}
            users.append(new_user)
            print("Ny bruker opprettet...")
            break
        else:
            print("""Passordende er ikke like.
            """)

def start_screen():
    print("""
1) Logg inn
2) Registrer bruker
0) Avlsutt""")
    valg = input("Hva ønsker du? ")
    print("")
    if valg == "1":
        login()
    elif valg == "2":
        create_user()
    elif valg == "0":
        return False
    return True

def main_screen():
    print("""
1) Generer en vits
0) Logg ut
""")
    valg = input("Hva ønsker du og gjøre? ")
    if valg == "0":
        return False
    return True
    
def main():
    global loggedInn
    run = True
    while run:
        if not loggedInn:
            run = start_screen()
        else:
            loggedInn = main_screen()

main()