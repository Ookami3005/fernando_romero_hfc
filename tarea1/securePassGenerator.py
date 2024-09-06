import random

# Pedimos los números de mayusculas, minúsculas y números que debe tener la contraseña
numMayus = int(input("Introduce el numero de mayusculas que debe tener la contraseña: "))
numMinus = int(input("Introduce el numero de minusculas que debe tener la contraseña: "))
numDigitos = int(input("Introduce el numero de digitos que debe tener la contraseña: "))

def randomUppercaseString(longitud):
    cadena = ""
    for i in range(0,longitud):
        cadena += chr(random.randint(65,90))
    return cadena

def randomLowercaseString(longitud):
    cadena = ""
    for i in range(0,longitud):
        cadena += chr(random.randint(97,122))
    return cadena

def randomNumberString(longitud):
    cadena = ""
    for i in range(0,longitud):
        cadena += str(random.randint(0,9))
    return cadena

def securePass(mayus, minus, nums):
    cadena = randomUppercaseString(mayus) + randomLowercaseString(minus) + randomNumberString(nums)
    lista = list(cadena)
    random.shuffle(lista)
    cadena = ""
    for i in lista:
        cadena += i
    return cadena

print("\nTe propongo la contraseña: "+securePass(numMayus,numMinus,numDigitos))

