# Operatører
plus = 31 + 450
minus = 102 - 200
gange = 32 * 32
modul = 11 % 2
a = 5
b = 3

print(f"""
--- Operatører ---
 - Regnestykker
Plus : {plus}
Minus : {minus}
Gange : {gange}
Modulus : {modul}

 - Variabler
{a == b}
{a > b}
{a > b}
""")

# If, Elif, Else
print("--- If, Elif, Else ---")
# user_age = int(input("Hvor gamel er du? : "))
user_age = 32
if user_age >= 15:
    print("Tillat")
elif user_age < 15:
    print("Ikke tillatt")
else:
    print("Pls skriv number")

# While-løkker
print("""
--- While-løkker ---
""")
tall = 5
while tall:
    tall = tall - 1
    if tall > 0:
        print(f"Tallet er {tall}")
    elif tall == 0:
        print("Ferdig!")


# For-løkker
# Oppgave 1
print("""
--- Før-løkker ---
 - Oppgave 1
""")
for number in range(1, 11):
    print(f"Number : {number}")

# Oppgave 2
print("""
 - Oppgave 2
""")
dyr = ["Hund", "Katt", "Hamster", "Slange", "Løve"]
for dyr in dyr:
    print(f"Dyret : {dyr}")

print("""
 - Oppgave 3
""")
for index in range(2, 11, 2):
    print(f"Partallet : {index}")

print("""
 - Oppgave 4
""")
for index in range(5, 0, -1):
    print(f"Tall : {index}")
    if index == 1:
        print("Ferdig!")

# Lister
print("""
--- Lister ---
""")
mat = ["Kebab", "Biff", "Hjemmelaget pizza"]
print(f"{mat[0]} og {mat[-1]}")
mat.append("Spaghetti")
mat.remove("Kebab")
print(f"Det er {len(mat)} matreter igjen, det er:")
for m in mat:
    print(f" - {m}")

# Dictionary
print("""
--- Dictionary ---
""")

megselv = {
    "navn" : "Ruben",
    "alder" : 17,
    "favorittfarge" : "Blå"
}
print(f"""Navn : {megselv["navn"]}
Alder : {megselv["alder"]}""")
megselv["favorittmatt"] = "Biff"
megselv["favorittfarge"] = "Rød"

print(f"""Nøkkler :
{megselv.keys()}

Verdier :
{megselv.values()}
""")

# Funksjoner
print("--- Funksjoner ---")
def lære_python():
    gjør_nå = "Hei, jeg lærer Python!"
    return gjør_nå

def to_x(tall):
    ganger_to = tall * 2
    return ganger_to

def to_tall_plus(tall1, tall2):
    total = tall1 + tall2
    return total

def areal(bredde, høyde):
    areal = bredde * høyde
    return areal

karakterer = [2, 5, 5, 4, 3, 6]
def karakter_kalulator():
    snitt = sum(karakterer) / len(karakterer)
    return snitt

print(f"""
{lære_python()}
{to_x(12)}
{to_tall_plus(5, 9)}
{areal(5, 20)}
{karakter_kalulator()}
""")