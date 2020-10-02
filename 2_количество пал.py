a = int(input())
b = c = 0
while b < a:
    z = 0
    b += 1
    x = b
    while x >= 1:
        z = z * 10 + x % 10
        x = x // 10
    if z == b:
        c += 1
print(c)
