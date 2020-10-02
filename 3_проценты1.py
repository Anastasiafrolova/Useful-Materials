import math
P = float(input())
X = float(input())
Y = float(input())
p = 1 + P / 100
XY = 100 * X + Y
XY1 = XY * p
X1 = XY1 // 100
Y1 = XY1 % 100
print(int(X1), int(Y1))
