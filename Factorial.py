
#1. Realiza un programa que calcule el factorial de un número introducido por el ususario.


num = int(input("Introduce un número para convertirlo a Factorial: "))
factorial = 1

if num<0:
    print("No puedes convertir un número negativo a factorial")

elif num == 0:
    print("El factorial de 0 es 1")

else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("El factorial de ", num, " es ", factorial)