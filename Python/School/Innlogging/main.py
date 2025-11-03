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
        print("Du er logget inn.")
        return "innlogget"
    elif valg == "2":
        print("Ny bruker registrert.")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("ugyldig svar, prøv igjen.")
        return "start"

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