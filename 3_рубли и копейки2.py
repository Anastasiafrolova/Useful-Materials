import math
n = float(input())
whole = math.floor(n)
kop = (n * 100) % 100
print(whole, round(kop))
