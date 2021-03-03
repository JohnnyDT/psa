# 1. cvicenie

# Zadanie prikladu:
# Nacitat meno a rok narodenia.
# Pozdravit uzivatela a vypocitat jeho vek (aktualny rok - rok narodenia)

import datetime

#kratsie riesenie
meno = input("Meno: ")
vek2 = (datetime.date.today().year) - int(input("Rok narodenia: "))
print("Ahoj " + meno + ", tvoj vek je: " + str(vek2) )


# krajsie riesenie
aktualny_rok = datetime.date.today().year

meno = input("Meno: ")
rok_narodenia = input("Rok narodenia: ")

vek = aktualny_rok - int(rok_narodenia)

print("Ahoj " + meno + ", tvoj vek je: " + str(vek) )
