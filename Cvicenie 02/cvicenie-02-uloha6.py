## ULOHA 6
# Budeme hrat takuto hru:
# kladiel vedla seba do radu mince s nahodnymi hodnotami z <1, 4>
# skoncim, ked ich sucet bude vacsi alebo rovnz danemu k
# Ak som skoncil so suctom, ktory je rovny k, vypise text 'HURA' inak 'SKODA'
# Napiste program, ktorz tuto hru odsimuluje 10-krat a vypise to pod seba

## Vystup pre k = 21 
# >>> print(prerob(12345678))
# '12_345_678'

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