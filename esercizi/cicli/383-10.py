#!/usr/bin/env python3

n = int(input("n: "))
base = int(input("base: "))
multiploCount = 0

for i in range(n):
    x = int(input("x: "))
    if x % base == 0:
        multiploCount += 1

print("Numeri multipli:", multiploCount)
