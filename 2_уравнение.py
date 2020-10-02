maximum = 0
num = 0
now = -1
while now != 0:
    now = int(input())
    if now > maximum:
        maximum, num = now, 1
    elif now == maximum:
        num += 1
print(num)
