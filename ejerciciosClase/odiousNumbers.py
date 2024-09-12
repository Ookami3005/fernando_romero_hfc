#!/usr/bin/python
# Hacking Fight Club

numOdiosos = [num for num in range(50) if bin(num).count('1') % 2 != 0]
dicc = dict([(a,(bin(a),hex(a))) for a in numOdiosos])
print(dicc)
