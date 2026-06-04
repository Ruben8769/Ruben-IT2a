import subprocess
import os
import json

ACTIVE_DIR = os.path.dirname(os.path.abspath(__file__))
create_one_user_file = os.path.join(ACTIVE_DIR, "createOneUser.ps1")
get_users = os.path.join(ACTIVE_DIR, "getOneUser.ps1")
json_data = os.path.join(ACTIVE_DIR, "polar_ansatte.json")

with open(json_data, "r") as d:
    json_list = json.load(d)

def create_user(firstname, surname, username, ou, email, phonenummber, jobtitle, department):
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", create_one_user_file,
        "-firstname", firstname,
        "-surname", surname,
        "-username", username,
        "-ou", ou,
        "-email", email,
        "-phonenummber", phonenummber,
        "-jobtitle", jobtitle,
        "-department", department,
    ])

def one_user():
    print("\n--- Create one user ---\n")
    create_user(input("Firstname: "), input("Surname: "), input("Username: "), input("OU: "), input("Email: "), input("Phonenummber"), input("Job Title: "), input("Department: "))

def user_from_json():
    print("\n--- User from JSON ---\n")
    for user in json_list["ansatte"]:
        firstname = user["fornavn"]
        surname = user["etternavn"]
        username = user["brukernavn"]
        split_username = username.split(".")
        completed_username = f"{split_username[0][0:3]}{split_username[1][0:3]}"
        ou = "OU=ExamTestTwo"
        email = user["epost"]
        phonenummber = user["telefon"]
        jobtitle = user["stilling"]
        department = user["avdeling"]
        create_user(firstname, surname, completed_username, ou, email, phonenummber, jobtitle, department)

def list_users():
    result = subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", get_users,
    ],
        capture_output=True,
        text=True
    )
    users = json.loads(result.stdout)
    for user in users:
        print(user)

print("\n--- Options ---\n  1. Create one user manualy\n    2. Add users from JSON\n    3. List users\n")
option = input("Choose: ")
if option == "1":
    one_user()
if option == "2":
    user_from_json()
if option == "3":
    list_users()
