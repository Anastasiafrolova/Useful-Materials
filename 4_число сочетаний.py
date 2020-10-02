n = int(input())
k = int(input())


def Cnk(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    if k == 0:
        return 1
    return Cnk(n - 1, k) + Cnk(n - 1, k - 1)


print(Cnk(n, k))
