#!/usr/bin/env python3

u0 = int(input("x: "))
u1 = int(input("y: "))
n = int(input("n: "))

l = [u0, u1]
for i in range(n - 2):
    l.append(l[-1] + l[-2])

print(l[n - 1])
