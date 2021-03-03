# 2. cvicenie - Zaklady Pythonu
print('------------------------------')

# CELE CISLA
# int - cele cislo (obmedzene len ramkou)
# rozne zapisy: desiatkova, binarna (0b11), oktalova - osmickova (0o11), hexadecimalna (0x11)
# Priklad: 3 + 8 + 11 - 2
print(0b11 + 0o10 + 0xB - 2)
print('------------------------------')

# DESATINNE CISLA
# obsahuju bodku (nie ciarku)
print (22/7)
print('------------------------------')

# KOMPLEXNE CISLA
# ako imaginarna jednotka sa pouziva znak "j"
# je potrebne importovat kniznicu
import cmath
print((2 + 3j) + (2 - 5j))
print('------------------------------')

# PRETYPOVANIE
# int(hodnota) - vyrobi cele cislo
# float(hodnota) - vyrobi desatinne cislo
# str(hodnota) - vyrobi retazec
print(type(str('123')))
print('------------------------------')

# RETAZCE
# String - str
# je to pole znakov (charakterov)
a = 'Hello World'
print(a[1])
print(len(a))

b = "Hello"
c = 'World'
print(b + c)
print(b + ' ' + c)
print(2 * b)
b = b + b       # vlozi dvakrat ten isty retazec
print('------------------------------')

# ESCAPE ZNAKY
# \'   - apostrof
# \\   - lomka
# \n   - novy riadok
# \t   - tabulator
print('Chcem napisat apostrof: \'')
print('------------------------------')

# PODRETAZCE
# za retazcom napiseme hranate zatvorky [start:end:step]
txt = 'abcdefgh'
print(txt[3:])
print(txt[:3])
print(txt[2:4])
print('------------------------------')

# ZOZNAMY
## list []
# utriedeny zoznam, ktory sa automatickz zvysuje alebo zmensuje
# moze obsahovat rozne typy premennnych 
# je mozne menit, mazat, ...
list1 = [1, 2, 'Ondrej', 3, 4, 5]
print(list1)
print(list1[1])
print('------------------------------')

## tuple ()
# nemenny utriedeny zoznam
# moze obsahovat rozne typy premennnych 
# nie je mozne menit, mazat, ...
tup1 = (1, 2, 'Ondrej', 3, 4, 5)
print(tup1)
print(tup1[2])
print('------------------------------')

## set {}
# neutriedeny zoznam
# nemoze obsahovat rozne typy premennnych 
set1 = {1, 3, 2}
print(set1)
print('------------------------------')

# LOGICKE OPERATORY

# VETVENIE - IF
cislo1 = 15
cislo2 = 20
if cislo1 > cislo2:
    print('Cislo1 > Cislo2')
elif cislo1 < cislo2:
    print('Cislo1 < Cislo2')
else:
    print('Cislo1 = Cislo2')

print('------------------------------')

# Cyklus FOR
# Python pozna IBA 'for each' cyklus !!
# pre predcasne ukoncenie treba pouzit BREAK alebo CONTINUE
ovocie = ["jablko", "banan", "paradajka"]
for x in ovocie:
    print(x)
print('----------')

for i in range(6):
    print(i)
print('----------')

for i in range(2, 10, 2):
    print(i)

print('------------------------------')

# Cyklus WHILE
xx = 0
while xx < 10:
    print(xx)
    xx += 1
    if xx == 5:
        break
print('------------------------------')

# PRACA SO SUBORMI

## Citanie zo suboru
# funkcia readline() precita jeden riadok zo suboru aj ukoncenie riadku
## Zapisovanie zo suboru
# funkcia write() zapise na koniec suboru (append)
## Zmazanie suboru
# potrebne importovat kniznicu "os" --> import os
# funkcia remove() 

# FUNKCIE
# Python je interpretovany jazyk, funkcia uz musi byt definovana uz v case volania (musi byt definovana nad volanim - vyssie v kode ako volanie)
def funkcia1():
    print("Zavolal som funkciu!")

funkcia1()
print('----------')

def scitaj(prve, druhe):
    sucet = prve + druhe
    return sucet

print(scitaj(1, 3))
print(scitaj("ano", "nie"))

print('------------------------------')

# TRIEDA
# je mozne definovat triedu s vlastnymi atributami a funkciami
# __init__