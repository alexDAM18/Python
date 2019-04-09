f =  open ("fichero.txt", "r")
leer = f.read()
count = 0
mayus = 0
minus = 0
palabras = 0

for i in leer:
    count += 1
    if i.isupper():
        mayus += 1
    if i.islower():
        minus += 1
    if i == ' ':
        palabras += 1


print("Hay un total de ", count, " letras")
print("Hay un total de ", mayus, " letras en mayúscula")
print("Hay un total de ", minus, " letras en minúscula")
print("Hay un total de ", palabras, " palabras")