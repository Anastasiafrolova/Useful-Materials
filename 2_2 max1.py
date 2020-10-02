i = int(input())
iMax1 = 0
iMax2 = 0
while i != 0:
    if (i >= iMax1) and iMax1 != 0 and iMax2 != 0:
        iMax2 = iMax1
        iMax1 = i
    if (iMax2 <= i <= iMax1) and iMax1 != 0 and iMax2 != 0:
        iMax2 = i
    i = int(input())
print(iMax2)
