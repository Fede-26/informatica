#!/usr/bin/env python3

saldo = 0
looping = True

while looping:
    n = int(input("n: "))
    saldo += n
    if n == 0:
        looping = False

print("Saldo intermedio:", saldo)

if saldo > 0:
    saldo += 0.015 * saldo
else:
    saldo += 0.03 * saldo

print("Saldo finale:", saldo)
