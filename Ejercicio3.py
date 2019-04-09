import operator

cadena = input("Introduce una cadena de texto: ")

voc = 0
cons = 0
mayus = 0
minus = 0
alfabeto  = {}


for i in cadena.replace(' ', ''):
    if i in "AaEeIiOoUu":
        voc=voc + 1

    else:
        cons=cons + 1

    if i.islower():
        minus=minus + 1

    if i.isupper():
        mayus=mayus + 1



    if i in alfabeto:
         alfabeto[i]=alfabeto[i] + 1
    else:
        alfabeto[i] = 1

alfabetOrd = sorted(alfabeto.items(), key=operator.itemgetter(0))

print("Vocales --> ", voc)
print("Consonantes --> ", cons)
print("Minúsculas --> ", minus)
print("Mayúsculas --> ", mayus)
print("Frecuencia: ")
for i in alfabetOrd:
    print(i)


