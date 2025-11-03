import random
max_tall = 200
gjettetall = random.randint(0, max_tall)
forsøk = 10

while forsøk > 0:
    gjett = int(input(f"Gjett tallet fra 0 til {max_tall}: "))
    if gjett == gjettetall:
        print("Du gjettet korekt.")
        break
    else:
        forsøk = forsøk - 1
        if gjett < gjettetall:
            print("Gjett høyere")
        elif gjett > gjettetall:
            print("Gjett lavere")
        print(f"{forsøk} forsøk igjen." )
    if forsøk == 0:
        print("Tom for forsøk, gjett på nytt.")