a = int(input())
if a % 3 == 0 or a % 5 == 0:
    answer = 'YES'
elif a % 5 % 3 == 0 or a % 3 % 5 == 0:
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
