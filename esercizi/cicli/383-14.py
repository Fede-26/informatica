#!/usr/bin/env python3


def cornice1():
    width = 0
    height = 0
    count = 0
    string = []

    while width < 3 and height < 3 and count <= 0:
        height = int(input("altez: "))
        width = int(input("largh: "))
        count = int(input("count: "))

    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1:
                string.append("*")
            elif j == 0 or j == width - 1:
                string.append("*")
            else:
                string.append("Q")
        string.append("\n")

    print(("".join(string)) * count)


def cornice2():  # non usa le liste
    width = 0
    height = 0
    count = 0

    while width < 3 and height < 3 and count <= 0:
        height = int(input("altez: "))
        width = int(input("largh: "))
        count = int(input("count: "))

    for c in range(count):
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1:
                    print("*", end="")
                elif j == 0 or j == width - 1:
                    print("*", end="")
                else:
                    print("Q", end="")
            print()


if __name__ == "__main__":
    cornice1()
    cornice2()
