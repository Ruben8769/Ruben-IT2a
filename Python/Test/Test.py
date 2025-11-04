import json

username = "Malware"
password = "123"
new_user = {"username":username, "password":password}

with open("Python/Test/Test.json", "r") as u:
    users = json.load(u)
print(users)

users.append(new_user)

with open("Python/Test/Test.json", "w") as u:
    json.dump(users, u, indent=4)