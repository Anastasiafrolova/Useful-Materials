from math import floor
n = float(input())
whole = floor(n)
kop = (n * 100) % 100
print(whole, int(kop))
