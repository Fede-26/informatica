#!/usr/bin/env python3

pari = 0
while 1:
    n = int(input("n: "))
    if (n%2 == 0):
        pari += 1
    else:
        break

print(pari)
