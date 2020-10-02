from math import sqrt, floor, ceil
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if a == 0 and b == 0 and c != 0:
    print(0)
elif a == b == c == 0:
    print('3')
elif a == 0:
    print('1', -c / b)
elif d < 0:
    print('0')
elif c == 0:
    x1 = 0
    x2 = - b / a
    if x1 > x2:
        print('2', x2, x1)
    else:
        print('2', x1, x2)
elif b == 0:
    print('2', - sqrt(-c / a), sqrt(-c / a))
elif b == c == 0:
    print('1', '0')
elif d == 0:
    x = - b / (2*a)
    print('1', x)
elif d > 0:
    x1 = (- b + sqrt(d)) / (2*a)
    x2 = (- b - sqrt(d)) / (2*a)
    if x1 > x2:
        print('2', x2, x1)
    else:
        print('2', x1, x2)
