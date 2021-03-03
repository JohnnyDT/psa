## ULOHA 4
# Napiste funkciu ciferny_sucet(cislo), ktora vypise ciferny sucet daneho cisla

## Vystup:
# >>> ciferny_sucet(11231)
# 8

print("\nULOHA 4 \n")

def ciferny_sucet(cislo):

    zadane_cislo = str(cislo)
    vysledok = 0

    for i in zadane_cislo:
        vysledok += int(i)

    print(vysledok)

ciferny_sucet(11231)