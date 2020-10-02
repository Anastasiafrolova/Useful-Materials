A = int(input())
B = int(input())
while A != B:
    if A % 2 != 0:
        A = A - 1
        print('-1')
    if A % 2 == 0 or (A == 2 and B == 1):
        A = A // 2
        print(':2')
