p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
xy = x * 100 + y
while i <= k:
    xy += int(xy * p / 100)
    i += 1
r = int(xy // 100)
k = xy % 100
print(r, k)
