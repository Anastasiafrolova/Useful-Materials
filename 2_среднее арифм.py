now = int(input())
if now % 2 == 0 and now != 0:
    n = 1
else:
    n = 0
while now != 0:
    now = int(input())
    if now % 2 == 0 and now != 0:
        n = n + 1
print(n)
