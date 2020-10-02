a = int(input())
b = int(input())
c = int(input())
d = int(input())
A = a < 0
B = a > 0
C = b < 0
D = b > 0
E = c < 0
F = c > 0
G = d < 0
H = d > 0
if A and C and E and G:
    answer = 'YES'
elif A and D and E and H:
    answer = 'YES'
elif B and C and F and G:
    answer = 'YES'
elif B and D and F and H:
    answer = 'YES'
else:
    answer = 'NO'
print(answer)
