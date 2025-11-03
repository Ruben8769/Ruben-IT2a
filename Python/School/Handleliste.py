shopping_list = []

run = True
while run:
    print("""
Velg en av de:
1. Se handleliste
2. Legg til vare
3. Fjern vare
4. Avslutt
    """)
    choice = int(input("Skriv valget : "))

    # Se handlelisten
    if choice == 1:
        if shopping_list == []:
            print("Handlelisten er tom.")
        else:
            print("Handleliste:")
            for content in shopping_list:
                print(f" - {content}")
    # Legge til varer i handlelisten
    elif choice == 2:
        add_shopping = input("Hva vil du legge til? : ")
        shopping_list.append(add_shopping)
    # Fjerne varer i handlelisten
    elif choice == 3:
        if shopping_list == []:
            print("Handlelisten er tom")
            pass
        else:
            print("Varer du kan fjerne:")
            for content in shopping_list:
                print(f" - {content}")
            remove_shopping = input("Hva vil du fjerne? : ")
            print(f"Fjernet {remove_shopping}.")
            shopping_list.remove(remove_shopping)
    # Gå ut av handlelisten
    elif choice == 4:
        run = False
    # Sjeker om valget er skrevet riktig
    else:
        print("Ta et valg fra listen.")