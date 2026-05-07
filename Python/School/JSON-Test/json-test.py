import json

with open("Python/School/JSON-Test/data.json", "r") as file:
    users = json.load(file)

for user in users["brukere"]:
    if user["alder"] > 20:
        print(f"Navn: {user["navn"]}\nAlder: {user["alder"]}")