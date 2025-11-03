brukere = []
run = True

while run:
    # Spør brukeren om valget
    print("""
    1. Legg til bruker
    2. Skriv ut brukere
    3. Avlsutt
    """)
    valg = input("Skriv valget ditt: ")
    if valg == "1":
        # Finner brukerverdier
        ny_bruker = {"fornavn" : "", "etternavn" : "", "tlf" : "", "adresse" : "", "epost" : ""}
        ny_bruker["fornavn"] = input("Fornavn: ")
        ny_bruker["etternavn"] = input("Etternavn: ")
        ny_bruker["tlf"] = int(input("Telefon numer: "))
        ny_bruker["adresse"] = input("Adresse: ")
        ny_bruker["epost"] = input("E-post: ")
        # Leger til brukerverdier
        brukere.append(ny_bruker)
        print("Bruker lagt til.")
    elif valg == "2":
        # Skriver ut hver bruker
        if brukere != []:
            for bruker in brukere:
                print(f"Navn : {bruker["fornavn"]} {bruker["etternavn"]}, Tlf : {bruker["tlf"]}, Adresse : {bruker["adresse"]}, E-post : {bruker["epost"]}")
        else:
            print("Bruker listen er tom.")
    elif valg == "3":
        # Avslutter programmet
        run = False
    else:
        print("Det valget finns ikke.")