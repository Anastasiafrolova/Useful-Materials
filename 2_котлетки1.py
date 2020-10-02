a = int(input())
b = int(input())
c = int(input())
d = c * 2 // a
if a >= c:
    answer = b * 2
elif c * 2 % a == 0:
    answer = d * b
else:
    answer = (d + 1) * b
print(answer)
