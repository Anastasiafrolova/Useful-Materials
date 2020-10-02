now = int(input())
nowMax = now
n = 0
while now != 0:
    if now > nowMax:
        nowMax = now
        n = 1
    elif now == nowMax:
        n = n + 1
    now = int(input())
print(n)
