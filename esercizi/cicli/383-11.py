#!/usr/bin/env python3

n = int(input("n: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
