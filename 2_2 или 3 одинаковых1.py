a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a == b and b != c or a == c and c != b or b == c and c != a:
    answer = '2'
elif a == b == c:
    answer = '3'
elif a != b and a != c and b != c:
    answer = '0'
print(answer)
