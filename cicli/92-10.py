#!/usr/bin/env python3

n = 101
while (n>100):
    n = int(input("n: "))

somma = 0

for i in range(n):
    x = int(input("x: "))
    if (x % 2 != 0):
        somma += x

print(somma)
