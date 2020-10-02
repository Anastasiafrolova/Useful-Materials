def gcd(a, b):
    if b == 0:
        return a
    if b != 0:
        return gcd(a, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
