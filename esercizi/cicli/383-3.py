#!/usr/bin/env python3

u0 = int(input("x: "))
u1 = int(input("y: "))
n = int(input("n: "))

for i in range(n - 2):
    u2 = u0 + u1
    u0 = u1
    u1 = u2

print(u2)
