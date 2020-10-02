a = int(input())
b = int(input())
c = int(input())
d = int(input())
A = a - c
B = b - d
if A <= 0:
    A = - A
else:
    A = A
if B <= 0:
    B = - B
else:
    B = B
if A % 2 == 0 and B % 2 == 0 or A % 2 != 0 and B % 2 != 0:
    answer = 'YES'
else:
    if A == B:
        answer = 'YES'
    else:
        answer = 'NO'
print(answer)
