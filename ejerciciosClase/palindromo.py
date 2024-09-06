#! /bin/python
# Hacking Fight Club

cadena = input()
cadenaReves = ""
for car in cadena:
    cadenaReves = car + cadenaReves

if (cadena == cadenaReves):
    print("Si es un palindromo!")
else:
    print("No es un palindromo!")
