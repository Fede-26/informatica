n = int(input("n: "))
count_pos = 0

for i in range(n):
    x = int(input("x: "))
    if (x>0):
        count_pos += 1

print(count_pos)