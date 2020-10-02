
f = 0
res = 1
f0 = 1
i = 0
while f <= n:
    res = f
    f = f0 + f
    f0 = res
    i += 1
    if n == f:
        print(i)
        break
if n < 0 or n != f:
    print(-1)
elif n == 0:
    print(0)
