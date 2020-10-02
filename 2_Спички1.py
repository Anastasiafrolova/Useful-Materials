l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
A = r1 - l1
B = r2 - l2
C = r3 - l3
if (l1 <= r2 and l2 <= r1 and l2 <= r3 and l3 <= r2)\
        or (l2 <= r1 and l1 <= r2 and l1 <= r3 and l3 <= r1)\
        or (l2 <= r3 and l3 <= r2 and l3 <= r1 and l1 <= r3)\
        or (l3 <= r2 and l2 <= r3 and l2 <= r1 and l1 <= r2)\
        or (l3 <= r1 and l1 <= r3 and l1 <= r2 and l2 <= r1)\
        or (l1 <= r2 and l3 <= r1 and l3 <= r2 and l2 <= r3):
    answer = '0'
else:
    if (l3 > r2 and A >= l3 - r2)\
            or (l2 > r3 and A >= l2 - r3)\
            or (l2 <= r3 and l3 <= r2):
        answer = '1'
    elif (l3 > r1 and B >= l3 - r1)\
            or (l1 > r3 and B >= l1 - r3)\
            or (l1 <= r3 and l3 <= r1):
        answer = '2'
    elif (l1 > r2 and C >= l1 - r2)\
            or (l2 > r1 and C >= l2 - r1)\
            or (l1 <= r2 and l2 <= r1):
        answer = '3'
    else:
        answer = '-1'
print(answer)
