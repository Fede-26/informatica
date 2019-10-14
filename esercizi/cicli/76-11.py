#!/usr/bin/env python3
#DOESN'T WORK

num = int(input("num: "))

def is_prime(n):
    if n > 1:
        for i in range(2, n//2):
            if (n % i) == 0:
                return False
            else:
                return True
    else:
        return False


i = 1
while (i <= num):
    if (is_prime(i)):
        print(i)
    i += 1
