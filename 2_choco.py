a = int(input())
b = int(input())
c = int(input())
if (c % a == 0 or c % b == 0) and c <= a * b:
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
