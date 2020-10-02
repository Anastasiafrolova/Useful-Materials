import math
P = float(input())
X = float(input())
Y = float(input())
p = 0.01 * P + 1
X1 = int(X * p) + (p * Y) // 100
Y1 = (X * p - int(X * p)) * 100 + (p * Y) % 100
print(int(X1), int(round(Y1)))
