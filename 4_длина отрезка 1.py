from math import sqrt


def dist(a, b, c, d):
    r = sqrt((c - a) ** 2 + (d - b) ** 2)
    return r


a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(dist(a, b, c, d))
