def ind(a, n):
    if n % 2 == 0:
        return ind(a ** 2, n / 2)
    else:
        return a * ind(a, n - 1)


a = ind(input())
n = float(input())
print(ind(a, n))
