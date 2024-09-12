#!/usr/bin/python
# Hacking Fight Club

import re

patron1 = r'[A-Z][a-z]+ [A-Z][a-z]+'
patron2 = r'@[\w]+'
patron3 = r'.*([A-Za-z]+.*\d+|\d+.*[A-Za-z]+).*'

resultado1 = re.search(patron1,'Nota del dia: Fernando Romero Cruz es un pendejo')
print(resultado1.group())

resultado2 = re.search(patron2,'Mi nombre de usuario es @ookami_5018, neta')
print(resultado2.group())

resultado3 = re.search(patron3, 'Una cadena sin numeros')
if resultado3:
    print(resultado3.group())
resultado4 = re.search(patron3, '123')
if resultado4:
    print(resultado4.group())
resultado5 = re.search(patron3, 'Hola123 _.@a')
if resultado5:
    print(resultado5.group())
