from math import sqrt

a = float(input())
b = float(input())
c = float(input())
D = (b * b - 4 * a * c)
x1 = x2 = 0
if D > 1:
    x2 = (-b + sqrt(D)) / (2 * a)
    x1 = (-b - sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif D == 0:
    x1 = x2 = -b / (2 * a)
    print(x1)
else:
    print('')
