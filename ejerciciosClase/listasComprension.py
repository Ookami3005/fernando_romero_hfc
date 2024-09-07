#!/usr/bin/python
# Hacking Fight Club

pares = [i for i in range(51) if i % 2 == 0]
print(pares)
print([i for i in range(51) if i not in pares])

lista2 = [i**2 for i in range(11)]
print(lista2)

lista3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print([[i+1 for i in sublist] for sublist in lista3])
