## ULOHA 1
# Napiste funkciu zoznam_cisel(retazec), ktora z daneho retazca vyrobi zoznam celych cisel.

## Vystup:
# >>> a = zoznam_cisel('12 345 6 -78 9000')
# >>> a
# [12 345 6 -78 9000]

print("\nULOHA 2 \n")

def zoznam_cisel(retazec):
  
    return list(map(int, retazec.split(' ')))

a = zoznam_cisel('12 345 6 -78 9000')
print(a)

