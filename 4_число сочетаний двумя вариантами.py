n = int(input())
k = int(input())


def factorial(n):
    if n == 0:
        return 1
    if n != 0:
        return n * factorial(n - 1)


def C(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    return factorial(n) / (factorial(k) * factorial(n - k))


def Cnk(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    return Cnk(n - 1, k) + Cnk(n - 1, k - 1)


print(C(n, k))
print(Cnk(n, k))
