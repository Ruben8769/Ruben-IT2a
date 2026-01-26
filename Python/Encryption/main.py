import sqlite3

conn = sqlite3.connect("Python/Encryption/database.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

encryption_key = 15

def retrive_account_data():
    sql_accounts = "SELECT name, password FROM accounts"
    accounts = cursor.execute(sql_accounts).fetchall()
    return accounts

def retrive_lg_name():
    sql_name_char = "SELECT characters FROM legal_char_name"
    lg_name_char = cursor.execute(sql_name_char).fetchall()
    return lg_name_char

def retrive_lg_password():
    sql_password_char = "SELECT characters FROM legal_char_password"
    lg_password_char = cursor.execute(sql_password_char).fetchall()
    return lg_password_char

def main():
    while True:
        print("\n- - - Velg - - -\n\n1. Login\n2. Legg til bruker\n")
        choice = input("Velg: ")
        if choice == "1":
            login()
        elif choice == "2":
            add_user()
        else:
            print("\nUgyldig inntastet, prøv på nytt.")

def encryption(encryption_key, password):
    password_list = list(password)
    for char in password_list:
        pass

def add_user():
    print("\n- - - Legg til bruker - - -\n")
    user_name = input("Navn: ")
    user_password = input("Passord: ")

def login():
    print("\n- - - Login - - -\n")
    user_name = input("Navn: ")
    user_password = input("Passord: ")

main()