""" Realiza un programa que convierte números decimales en numeración romana y viceversa.
Consideraremos que el usuario introduce bien el número y que como máximo el número sea
igual a 4000"""

values = (('M', 1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))

def RomanToInt(rom_num):
    result = 0
    lista = []
    for i in range(len(rom_num)):
        for letter, value in values:
            if rom_num[i] == letter:
                lista.append(value)
    lista.append(0)
    for i in range(len(rom_num)):
        if lista[i] >= lista[i+1]:
            result = result + lista[i]
        else:
            result = result - lista[i]
    return result

def int_to_roman(dec_num):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(dec_num) / int(ints[i])
        result += nums[i] * int(count)
        dec_num = int(dec_num) - int(ints[i] * int(count))
    return result

print("Conversión de numeros ")
print("")
print("1 - De romano a decimal.")
print("2 - De decimal a romano.")
print("")
opcion = input("Elige la conversión que desea realizar: ")


if opcion == "1":

    numRom = input("Introduce un número romano: ").upper()

    print(numRom, " --> ", RomanToInt(numRom))


if opcion == "2":
     numDec = input("Introduce un número decimal: ").upper()
     print(numDec, " --> ", int_to_roman(numDec))










