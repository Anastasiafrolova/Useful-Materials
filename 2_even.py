a = int(input())
b = int(input())
c = int(input())
A = a % 2
B = b % 2
C = c % 2
if (A == 0 or B == 0 or C == 0) and (A != 0 or B != 0 or C != 0):
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
