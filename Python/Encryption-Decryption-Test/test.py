import json

with open("Python/Encryption-Decryption-Test/Legal-ch.json", "r") as lch: legal_chs = json.load(lch)

user_password = input("Password: ")
user_password_list = list(user_password) # Sjeker om passored bruker lovelig tegn

allowed_ch = []
for user_ch in user_password_list:
    for legal_ch in legal_chs:
        if user_ch == legal_ch:
            allowed_ch.append(True)
            break
    else: allowed_ch.append(False)

print(allowed_ch)

for character in allowed_ch:
    if character == False:
        break
else:
    pass