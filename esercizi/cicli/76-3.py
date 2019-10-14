#!/usr/bin/env python3

n = 5
minimo = 10
massimo = 100

count = minimo
somma = 0

while (count <= massimo):
    if (count%n == 0):
        somma += count
    count += 1

print(somma)
