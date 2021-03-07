## ULOHA 3
# Napiste funkciu vyhod_none(ntica), ktora z danej n-tice vyhodi vsetky vyskyty None.
# Funkcia vrati (return) tuto novu n-ticu (nic nevypisuje).
# n-tica -> tuple 

## Vystup:
# >>> print(vyhod_none(None, 1, None, None))
# (1,)

## tuple ()
# nemenny utriedeny zoznam
# nemozme menit, mazat ani pridavat prvky
# ak chceme upravovat tak prekonvertovat na list --> upravit --> prekonevertovat naspat na tuple

print("\nULOHA 3 \n")

def vyhod_none(*args):              # function recieve a TUPLE of arguments

    pomocny_list = []

    for i in args:
        if i != None:
            pomocny_list.append(i)

    return tuple(pomocny_list)

print(vyhod_none(None, 1, "aloha", None, -4588, "Peter"))