a = int(input())
b = int(input())
c = int(input())
if a < c:
    d = c * 2 // a
    if c * 2 % a == 0:
        answer = d * b
    if c % a != 0:
        answer = (d + 1) * b
elif a >= c:
    answer = b * 2
print(answer)
