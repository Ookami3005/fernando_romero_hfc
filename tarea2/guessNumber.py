#!/usr/bin/python
# Hacking Fight Club

from random import randint

print('Generando número secreto...')
numSecreto = randint(1,100)

num = 0

while(num != numSecreto):
    print("\nAdivina el numero secreto!!")
    num = int(input("Que numero piensas que es?: "))

    if num == numSecreto:
        print('\nCorrecto!!! El numero era %s :)' % numSecreto)
    elif num > numSecreto:
        print('\nIncorrecto! Intenta con un numero mas chico')
    else:
        print('\nIncorrecto! Intenta con un numero mas grande')
