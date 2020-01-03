#!/usr/bin/env python3

c = input("c: ")
n = int(input("n: "))

for i in range(1, n * 2 + 1, 2):  # start to 1 and goes n times with step of 2
    curr_line = c * i  # repeats the current char by i times
    curr_line = curr_line.center((n * 2) - 1, " ")  # center the string
    print(curr_line)
