import math
def length(a, b, c, d):
    A = b - a
    B = d - c
    return math.sqrt((A ** 2) + (B ** 2))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(length(a, b, c, d))
