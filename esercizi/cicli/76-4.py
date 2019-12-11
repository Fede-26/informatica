#!/usr/bin/env python3

def is_prime(x):
    if  (x == 2):
        return True

    for i in range(2, x):
        if (x%i == 0):
            return False
        return True

num = int(input("num: "))

count = 0
while (count<num):
    if (is_prime(count)):
        print(count)
    count += 1
