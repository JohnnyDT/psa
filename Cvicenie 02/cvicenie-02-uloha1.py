## ULOHA 1
# Sportovec prve den prebehol x kilometro.
# Kazdy dalsi den prebehol o 10% viac ako v predchadyajuci den.
# Napiste program, ktory pre dane y zisti, v ktory den sportovec dokopy prebehne aspon y kilometrov.
# (Ktory den prekroci planovanych cielovych zadanych KM)

## Vystup:
# Zadaj km pre prvy den: 10
# Zadaj cielovy pocet km: 20
# na 9.den prebehne 21.44 km

print("\nULOHA 1 \n")

narast = 1.1                                            # narast na dalsi den 10% (vynasobenie 1.1)
km_prvy_den = int(input("Zadaj km pre prvy den: "))     # pocet km v prvy en
km_cielove = int(input("Zadaj cielovy pocet km: "))     # pocet cielovych km

km_nasledujuci_den = km_prvy_den
den = 1

while km_nasledujuci_den < km_cielove:
    den = den + 1
    km_nasledujuci_den = km_nasledujuci_den * narast
    print("\tna " + str(den) + ".den prebehne " + str(km_nasledujuci_den) + " km")