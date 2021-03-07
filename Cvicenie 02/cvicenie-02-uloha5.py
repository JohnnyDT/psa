## ULOHA 5
# Napiste funkciu prerob(cislo), ktora z daneho celeho cisla vyrobi retazec,
# ale tak, ze cifry zoskupi do trojic (sprava) a oddeli podciarkovnikom.
# Funkcia nic nevypisuje, ale vrati (return) vysledny retazec.

## Vystup:
# >>> print(prerob(12345678))
# '12_345_678'

# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |         pole
# | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |         hodnoty
#             *           *                 za ktory index vlozit (index % 3 = zvysok 2)
# | 8 | 7 | 6|_|5 | 4 | 3|_|2 | 1 |         hodnoty s podciarkami

print("\nULOHA 5 \n")

def prerob(cislo):

    novy_retazec = ('')
    retazec = str(cislo)

    x = len(retazec)             # dlzka povodneho retazca    
    while x > 0:
        x -= 1
        novy_retazec += retazec[x]
        if x % 3 == 2:
            novy_retazec += "_"

    return novy_retazec [::-1]    
    #   [::-1] ----> vypis odzadu 
    #   [start:end:step]

print(prerob(12345678))