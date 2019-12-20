#!/usr/bin/env python3

n1 = int(input("n1: "))
n2 = int(input("n2: "))
risultato = 0
resto = n1

while resto >= n2:
    resto -= n2
    risultato += 1

print("risultato:", risultato)
print("resto:", resto)
