a = int(input())
if a % 3 == 0 or a % 5 == 0:
    answer = 'YES'
elif a % 3 % 2 == 0 and a > 3 or a % 5 % 3 == 0 or a % 5 == 1 and a > 5:
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
