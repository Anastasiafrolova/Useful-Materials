a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c
    if b >= c
        print(c, b, a)
elif a >= c >= b:
    answer = b, c, a
elif b >= c >= a:
    answer = a, c, b
elif b >= a >= c:
    answer = c, a, b
elif c >= a >= b:
    answer = b, a, c
elif c >= b >= a:
    answer = a, b, c
print(answer)
