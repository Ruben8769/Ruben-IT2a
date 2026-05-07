import json

def read_data():
    with open("Python/School/JSON-Test/bildeler.json", "r") as data:
        return json.load(data)

def main():
    while True:
        global car_data
        car_data = read_data()
        print("""
====== Startmeny ======\n
    1. Skriv ut
    2. Finn deler i en kategori
    3. Deler med lav lagerstatus
    4. Legg til ny bildel
    5. Finn gjennomsnittspris
""")
        choice = input("Velg: ")
        if choice == "1":
            print_out()
        elif choice == "2":
            find_part()
        elif choice == "3":
            low_amount()
        elif choice == "4":
            add_part()

def print_out():
    print(f"\n====== Deler ======\n\nVerksted        :  {car_data["verksted"]}\nSist oppdatert  :  {car_data["sistOppdatert"]}")
    for data in car_data["deler"]:
        print(f"\nNavn    :  {data["navn"]}\nPris    :  {data["pris"]}\nAntall  :  {data["antallPaLager"]}")

def find_part():
    print("\n====== Del Fra Kategori ======\n")
    user_part = input("Navn på bildel: ")
    for data in car_data["deler"]:
        if data["kategori"] == user_part:
            print(f"\nNavn   :  {data["navn"]}\nLager  :  {data["antallPaLager"]}")

def low_amount():
    print("\n====== Lav lagerstatus ======\n")
    low_warning_limit = 20
    for data in car_data["deler"]:
        if data["antallPaLager"] < low_warning_limit:
            print(f"\nNavn    :  {data["navn"]}\nAntall  :  {data["antallPaLager"]}")

def add_part():
    print("\n====== Legg Til Bildel ======\n")
    new_part_list = []
    user_id = 1 + (car_data["deler"][-1]["id"])
    user_name = input("Navn: ")
    user_category = input("Kategori: ")
    user_pris = input("Pris: ")
    user_storage = input("Antall: ")
    user_brand = input("Leverandør: ")
    user_brand = input("Passer til: ")

    

main()