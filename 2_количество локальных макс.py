a = int(input())
b = int(input())
c = int(input())
n = 2
time1 = 0
time2 = 0
i = 0
j = 0
locMaxCount = 0
while a != 0 and b != 0 and c != 0:
    n += 1
    if a < b > c:
        locMaxCount += 1
        time2 = time1
        time1 = n - 1
        if locMaxCount > 1:
            i = time1 - time2
            if j == 0:
                j = i
                i = 0
            else:
                if j > i:
                    j = i
                    i = 0
    (a, b) = (b, c)
    c = int(input())
print(j)
