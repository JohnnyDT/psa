## ULOHA 1
# Sportovec prvy den prebehol x kilometrov.
# Kazdy dalsi den prebehol o 10% viac ako v predchadzajuci den.
# Napiste program, ktory pre dane y zisti, v ktory den sportovec dokopy prebehne aspon y kilometrov.
# (Ktory den konecne prekroci planovanych cielovych zadanych KM) --> nie spolu ale za jeden den

## Vystup:
# Zadaj km pre prvy den: 10
# Zadaj cielovy pocet km: 20
# na 9.den prebehne 21.44 km

print("\nULOHA 1 \n")

narast = 1.1                                            # narast na dalsi den 10% (vynasobenie 1.1)
km_odbehnute = int(input("Zadaj km pre prvy den: "))    # pocet km v prvy en
km_cielove = int(input("Zadaj cielovy pocet km: "))     # pocet cielovych km

den = 1

while km_odbehnute < km_cielove:
    den += 1
    km_odbehnute *= narast                              # Floating Point Math

print("---> na " + str(den) + ".den prebehne " + str(round(km_odbehnute, 2)) + " km")