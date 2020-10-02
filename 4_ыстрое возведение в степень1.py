def index(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return index(a ** 2, n / 2)
    elif n % 2 != 0:
        return a * index(a, n - 1)


a = float(input())
n = int(input())
print(index(a, n))
