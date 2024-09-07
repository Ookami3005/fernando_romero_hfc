#!/usr/bin/python
# Hacking Fight Club

var=map((lambda x: x.upper()),(filter((lambda x: 'i' in str(x)),((lambda a,b,c,d: a+b+c+d)([1,2,3,4],["Hackers","Fight","Club"],["Piccoro","Goku","Videl","Babidi","Broly"],["Python","Rust","Kotlin",""])))))

for i in var:
    print(i)
