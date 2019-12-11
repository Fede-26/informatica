#!/usr/bin/env python3
i = -1
while i < 1:
    i = int(input("i: "))

c = 0
while c < i:
    n = int(input("n: "))
    if c == 0:
        minimo = n
        massimo = n

    if n > massimo:
        massimo = n
    elif n < minimo:
        minimo = n
    c += 1

print("minimo:", minimo)
print("massimo:", massimo)