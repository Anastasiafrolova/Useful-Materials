import math
n = float(input())
b = int(round(n % 1, 5) * 10)
if b < 5:
    print(math.floor(n))
elif b >= 5:
    print(math.ceil(n))
