# Importering
import datetime
import sqlite3


# Kobler til SQLite database
conn = sqlite3.connect("Python/School/Skolebiblotek/database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")
sql_books = cursor.fetchall()

cursor.execute("SELECT * FROM students")
sql_students = cursor.fetchall()

cursor.execute("SELECT * FROM borrowing")
sql_borrowing = cursor.fetchall()


# Lager globale variabler
run = True

# Lager funksjoner
# Funksjonen for og kjøre alt
def main():
    while run:
        start_menu()


# Startfunksjonen
def start_menu():
    print("\n--- Start Meny ---\n  1. Registrer bok\n  2. Registrer elev\n  3. Lån/lever bok\n")
    user_answer = input("Velg: ")
    if user_answer == "1":
        register_bok()
    elif user_answer == "2":
        register_student()
    elif user_answer == "3":
        book_borrow()
    else:
        print("\nUgyldig inntastet, prøv på nytt.")


# Funkjson for registrering av bok
def register_bok():
    pass


# Funksjon for registrering av elev
def register_student():
    pass


# Funksjon for lån/lever bok
def book_borrow():
    pass


main()