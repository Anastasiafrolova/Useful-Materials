import math


def IsPointInCircle(x, y, xc, yc, r):
    x1 = xc - x
    y1 = yc - y
    lxy = math.sqrt(x1 ** 2 + y1 ** 2)
    return lxy <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
