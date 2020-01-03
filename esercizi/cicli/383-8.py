#!/usr/bin/env python3

n = int(input("n: "))
pariCount = 0
dispariCount = 0

for i in range(n):
    x = int(input("x: "))
    if x % 2 == 0:
        pariCount += 1
    else:
        dispariCount += 1

dispariPerc = dispariCount / n * 100
print("N pari:", pariCount)
print("N% dispari:", dispariPerc)
