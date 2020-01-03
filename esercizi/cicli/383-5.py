#!/usr/bin/env python3

pari = 0
pariCount = 0
dispari = 0
dispariCount = 0

for i in range(int(input("n: "))):
    x = int(input("x: "))
    if x % 2 == 0:
        pari += x
        pariCount += 1
    else:
        dispari += x
        dispariCount += 1

print("Media pari:", pari / pariCount)
print("Media dispari:", dispari / dispariCount)
