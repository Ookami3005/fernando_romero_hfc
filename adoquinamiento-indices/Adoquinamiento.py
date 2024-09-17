#!/usr/bin/python3
# Adoquinamiento basado en la idea de Danna Lizette Márquez Corona

from random import randrange
from termcolor import colored

"""
Función que inicializa una matriz vacía que representa el tablero
"""
def inicializa_tablero(n):
    matriz = [[-1]*(2**n) for _ in range(2**n)]
    return matriz

"""
Función que interpreta los números que representan adoquines y le da formato
para imprimirlo en pantalla
"""
def imprime_tablero(tablero):

    """
    Diccionario de colores disponibles
    """
    colores = {
        1:'dark_grey',
        2:'blue',
        3:'yellow',
        4:'green',
        5:'magenta',
        6:'cyan',
        7:'red'
    }

    """
    Impresión del tablero en base al mapeo de los números para asignarles
    su respectiva representación y color
    """
    for l in tablero:
        items = map((lambda x: 'O' if x == -1 else (colored('X','red') if x == 0 else colored('O',colores[x % 7 + 1]))), l)
        for i in items:
            print(f"{i} ", end='')
        print()

"""
Contador global del número de adoquines utilizados
"""
contador_adoquin = 1

"""
Algoritmo de adoquinamiento sobre una matriz
"""
def adoquinamiento(tablero, x, y, marca, tam):

    # Recuperamos el contador global
    global contador_adoquin

    """
    Caso base: El cuadrante es de 1x1
    """
    if tam == 1:
        return

    """
    Declaración de variables necesarias
    """
    mitad = tam // 2
    marca_x, marca_y = marca
    mitad_x, mitad_y = (x+mitad,y+mitad)
    bot_der = (marca_x >= mitad_x, marca_y >= mitad_y)
    
    """
    División de casos para la casilla marcada y llamadas recursivas
    reajustando subcuadrantes y marcas
    """
    if bot_der == (0,0):
        tablero[mitad_x-1][mitad_y] = contador_adoquin
        tablero[mitad_x][mitad_y-1] = contador_adoquin
        tablero[mitad_x][mitad_y] = contador_adoquin
        contador_adoquin += 1
        adoquinamiento(tablero, x, y, marca, mitad)
        adoquinamiento(tablero, x, y+mitad, (mitad_x-1, mitad_y), mitad)
        adoquinamiento(tablero, x+mitad, y, (mitad_x, mitad_y-1), mitad)
        adoquinamiento(tablero, x+mitad, y+mitad, (mitad_x, mitad_y), mitad)
    elif bot_der == (1,0):
        tablero[mitad_x-1][mitad_y-1] = contador_adoquin
        tablero[mitad_x-1][mitad_y] = contador_adoquin
        tablero[mitad_x][mitad_y] = contador_adoquin
        contador_adoquin += 1
        adoquinamiento(tablero, x, y, (mitad_x-1, mitad_y-1), mitad)
        adoquinamiento(tablero, x, y+mitad, (mitad_x-1, mitad_y), mitad)
        adoquinamiento(tablero, x+mitad, y, marca, mitad)
        adoquinamiento(tablero, x+mitad, y+mitad, (mitad_x, mitad_y), mitad)
    elif bot_der == (0,1):
        tablero[mitad_x-1][mitad_y-1] = contador_adoquin
        tablero[mitad_x][mitad_y-1] = contador_adoquin
        tablero[mitad_x][mitad_y] = contador_adoquin
        contador_adoquin += 1
        adoquinamiento(tablero, x, y, (mitad_x-1,mitad_y-1), mitad)
        adoquinamiento(tablero, x, y+mitad, marca, mitad)
        adoquinamiento(tablero, x+mitad, y, (mitad_x, mitad_y-1), mitad)
        adoquinamiento(tablero, x+mitad, y+mitad, (mitad_x, mitad_y), mitad)
    else:
        tablero[mitad_x-1][mitad_y-1] = contador_adoquin
        tablero[mitad_x][mitad_y-1] = contador_adoquin
        tablero[mitad_x-1][mitad_y] = contador_adoquin
        contador_adoquin += 1
        adoquinamiento(tablero, x, y, (marca_x-1,marca_y-1), mitad)
        adoquinamiento(tablero, x, y+mitad, (mitad_x-1, mitad_y), mitad)
        adoquinamiento(tablero, x+mitad, y, (mitad_x, mitad_y-1), mitad)
        adoquinamiento(tablero, x+mitad, y+mitad, marca, mitad)


"""
****************************
Función principal del script
****************************
"""
def main():
    # Requerimos la potencia de 2 al usuario
    print('*Bienvenido*')
    print('Crearé un tablero de 2^n * 2^n para adoquinarlo!')
    print('> La casilla marcada inicial será generada aleatoriamente')
    dim = int(input("Introduce la potencia de 2: "))

    # Marcamos una casilla aleatoriamente
    tablero = inicializa_tablero(dim)
    a,b = (randrange(2**dim), randrange(2**dim))
    tablero[a][b] = 0

    # Mostramos el tablero inicial y el resuelto al usuario
    print()
    print('Tablero inicial:\n')
    imprime_tablero(tablero)
    print()
    adoquinamiento(tablero, 0, 0, (a,b), 2**dim)
    print('Tablero adoquinado:\n')
    imprime_tablero(tablero)

if __name__ == "__main__":
    main()
