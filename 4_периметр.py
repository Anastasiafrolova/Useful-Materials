from math import sqrt


def dist(x1, y1, x2, y2, x3, y3):
    AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    BC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    AC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    P = AB + BC + AC
    return P


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
print(dist(x1, y1, x2, y2, x3, y3))
