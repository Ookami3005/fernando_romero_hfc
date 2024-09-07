#!/usr/bin/python
# Hacking Fight Club

print((lambda x,y,z: x*y*z)(2,3,4))
print((lambda x: x==[])([1,2]))
print((lambda x: x==[])([]))
print((lambda x,y: len(x) >= y)([1,2,3,4],4))
print((lambda x,y: len(x) >= y)([1,2,3,4],6))
print((lambda x: x**(0.5))(4))
print((lambda x,y: x.intersection(y))({1,2,3},{3,4,5}))
