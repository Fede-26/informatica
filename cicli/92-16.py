n = int(input("n: "))
divisori = []

for i in range(1, n+1):
    if (n%i == 0 and i != 0):
        divisori.append(i)

print(sum(divisori)/len(divisori))