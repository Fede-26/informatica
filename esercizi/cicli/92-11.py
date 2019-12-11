#!/usr/bin/env python3

n = int(input("n: "))
x = int(input("x: "))

maggiore_di_x = 0
uguali_a_x = 0
minore_di_x = 0

for count in range(n):
    num_input = int(input("num_input: "))
    if (num_input>x):
        maggiore_di_x += 1
    elif (num_input==x):
        uguali_a_x += 1
    elif (num_input<x):
        minore_di_x += 1

print(maggiore_di_x, uguali_a_x, minore_di_x)
