import json

with open("Python/Encryption-Decryption-Test/Legal-ch.json", "r") as lch:
    legal_chs = json.load(lch)

encryption_key = 5
user_password = list(input("Password: "))

# Sjeker om passored bruker lovelig tegn
allowed_ch = []
for user_ch in user_password:
    for legal_ch in legal_chs:
        if user_ch == legal_ch:
            allowed_ch.append(True)
            break
    else: allowed_ch.append(False)

# Koden som encrypterer bruker passored
for character in allowed_ch:
    if character == False:
        break
else:
    position = []
    new_postion = []
    encryptet_chars = []
    for us_ch in user_password:
        index_value = legal_chs.index(us_ch)
        position.append(index_value)
    for pos in position:
        new_pos = (pos + encryption_key) % len(legal_chs)
        new_postion.append(new_pos)
        encryptet_chars.append(legal_chs[new_pos])
    encryptet_passwords = "".join(encryptet_chars)

# Koden som decrypterer bruker passored
