#!/usr/bin/python
# Hacking Fight Club

# Lectura del archivo con palabras
reader = open('palabras.txt', 'r')
contenido = reader.readlines()
reader.close()

# Reglas de conversion de las palabras para generar las contraseñas
conversiones = {
    'a':'@',
    'i':'1',
    'e':'3',
    '0':'o',
    'u':'v',
    'v':'b',
    's':'5',
    'r':'R',
    'k':'K',
    'K':'k'
}

# Acumulador de las contraseñas
nuevoContenido = ""

# Definición del escritor
writer = open('contraseñas.txt', 'w')

# Aplicación de las conversiones
for linea in contenido:
    for car in linea:
        if car in conversiones:
            nuevoContenido += conversiones[car]
        else:
            nuevoContenido += car

# Escritura de las contraseñas
writer.write(nuevoContenido)
