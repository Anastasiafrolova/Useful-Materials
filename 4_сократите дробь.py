n = int(input())
m = int(input())


def gcd(n, m):
    if m == 0:
        return n
    if m != 0:
        return gcd(n, n % m)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


print(*ReduceFraction(n, m))
