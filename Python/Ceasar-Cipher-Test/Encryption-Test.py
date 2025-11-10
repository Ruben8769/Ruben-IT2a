import json

with open("Python/Test/Legal-ch.json", "r") as lch:
    legal_chs = json.load(lch)

user_password = input("Password: ")

allowed_ch = []  
for user_ch in list(user_password):
    for legal_ch in legal_chs:
        if user_ch == legal_ch:
            allowed_ch.append(True)
            break
    else:
        allowed_ch.append(False)

print(allowed_ch)