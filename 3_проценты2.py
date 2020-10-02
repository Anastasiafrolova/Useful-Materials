p = float(input())
x = float(input())
y = float(input())
xy = x * 100 + y
xyp = xy * p / 100
xy += xyp
r = int(xy // 100)
k = int(xy % 100)
print(r, k)
