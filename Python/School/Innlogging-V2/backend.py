# Importerer moduler
import json

# Importerer data
with open("Python/School/Innlogging-V2/brukerdata.json", "r") as us:
    user_data = json.load(us)

with open("Python/School/Innlogging-V2/lovlige-tegn.json", "r") as lc:
    legal_chs = json.load(lc)

# Variabler
CRYPTO_KEY = 5

# Funksjoner
"""
    legal_str():
        return True - Ingen ulovlige tegn funnet
        return False - Ulovlige tegn funnet
    
    encryption():
        return encryptet_psw - Retunerer passored som enkryptert
    
    matching_usr_psw():
        return True - Brukernavn og passord korrekt
        return False - Brukernavn eller passordet er ikke korrekt, eller ikke funnet.

    matching_user():
        return True - Brukernavn funnet
        return False - Brukernavn ikke funnet
"""

def legal_str(string):
    user_psw = list(string)
    for user_ch in user_psw:
        for legal_ch in legal_chs:
            if user_ch == legal_ch:
                break
        else:
            return False
    return True

def encryption(encryption_str):
    user_psw = list(encryption_str)
    position = []
    encryptet_ch = []
    for user_ch in user_psw:
        index_value = legal_chs.index(user_ch)
        position.append(index_value)
    for pos in position:
        new_pos = (pos + CRYPTO_KEY) % len(legal_chs)
        encryptet_ch.append(legal_chs[new_pos])
    encryptet_psw = "".join(encryptet_ch)
    return encryptet_psw

def matching_usr_psw(user_username, encryptet_psw):
    for user in user_data:
        if user["username"] == user_username:
            if user["password"] == encryptet_psw:
                return True
    else:
        return False

def matching_usr(user_username):
    for user in user_data:
        if user["username"] == user_username:
            return True
    else:
        return False

def dump_data(user_username, user_password):
    new_user = {"username":user_username, "password":encryption(user_password)}
    user_data.append(new_user)
    with open("Python/School/Innlogging-V2/brukerdata.json", "w") as us:
        json.dump(user_data, us, indent=4)