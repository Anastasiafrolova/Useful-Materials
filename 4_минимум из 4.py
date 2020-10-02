def minfour(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    return min(min1, min2)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(minfour(a, b, c, d))
