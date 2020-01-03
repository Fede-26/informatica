#!/usr/bin/env python3

n = int(input("n: "))
prodPos = 0
prodNeg = 0
prodZero = 0

for i in range(n):
    x = int(input("x: "))
    y = int(input("y: "))
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        prodPos += 1
    elif (x > 0 and y < 0) or (x < 0 and y > 0):
        prodNeg += 1
    else:
        prodZero += 1

print("Coppie con prodotto positivo:", prodPos)
print("Coppie con prodotto negativo:", prodNeg)
print("Coppie con prodotto zero:", prodZero)
