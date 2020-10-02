K = int(input())
a = 1
b = 0
n = 0
while a <= K:
    ost = a % 10
    a = a // 10
    b = b * 10
    b = b + ost
    if b <= K:
        n = n + 1
print(n)
