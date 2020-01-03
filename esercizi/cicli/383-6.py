#!/usr/bin/env python3

votiCount = 7
voti = 0

for i in range(votiCount):
    voti += int(input("Voto: "))

print("Media voti:", voti / votiCount)
