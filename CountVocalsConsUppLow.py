cadena = input("Introduce una cadena de texto: ")

voc = 0
cons = 0
mayus = 0
minus = 0

for i in cadena.replace(' ', ''):
    if i in "AaEeIiOoUu":
        voc = voc + 1

    else:
        cons = cons + 1

    if i.islower():
        minus = minus + 1

    if i.isupper():
        mayus = mayus + 1




print("Vocales --> ", voc)
print("Consonantes --> ", cons)
print("Minúsculas --> ", minus)
print("Mayúsculas --> ", mayus)