a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (a <= d or a <= e) and (b <= d or b <= e):
    answer = 'YES'
elif (a <= d or a <= e) and (c <= d or c <= e):
    answer = 'YES'
elif (c <= d or c <= e) and (b <= d or b <= e):
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
