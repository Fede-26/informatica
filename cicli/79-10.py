num = int(input("num: "))

somma = 0
count = 0
while (count<num):
    if (count%2 == 0):
        somma += count
    count += 1

print(somma)