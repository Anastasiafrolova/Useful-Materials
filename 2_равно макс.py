x = int(input())
max1 = x
len1 = 1
while x != 0:
    x = int(input())
    if x > max1:
        max1 = x
        len1 = 1
    elif x == max:
        len1 += 1
print(len1)
