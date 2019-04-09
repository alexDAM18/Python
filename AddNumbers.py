"""2. Crea un programa que pida dos números enteros y realice la suma de todos los números
pares comprendidos entre ellos."""

num1 = int(input("Introduce un primer número: "))
num2 = int(input("Introduce un segundo número: "))
suma = 0

for i in range (num1, num2):
    if i % 2 == 0:
        suma = suma + i

print("La suma es: ", suma)