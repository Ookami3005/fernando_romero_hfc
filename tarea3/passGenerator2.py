#!/usr/bin/python
# Hacking Fight Club

reader = open('palabras.txt', 'r')
contenido = reader.readlines()
reader.close()

for linea in contenido:
    print("BOF")
    print(linea+"EOF\n")
