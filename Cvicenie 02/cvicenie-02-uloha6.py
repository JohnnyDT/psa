## ULOHA 6
# Budeme hrat takuto hru:
# kladiem vedla seba do radu mince s nahodnymi hodnotami z <1, 4>
# skoncim, ked ich sucet bude vacsi alebo rovny danemu k
# Ak som skoncil so suctom, ktory je rovny k, vypise text 'HURA' inak 'SKODA'
# Napiste program, ktory tuto hru odsimuluje 10-krat a vypise to pod seba.

import random

k = int(input("Zadaj k: "))

for i in range(10): 

    sucet = 0
    while sucet < k:
        vygenerovane_cislo = random.randrange(1, 5)
        print(str(vygenerovane_cislo) + ",", end = " ")
        sucet += vygenerovane_cislo

    if sucet == k:
        print("  HURA")
    else:
        print("  SKODA")