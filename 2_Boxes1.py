a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
A1 = a1 <= a2 and b1 <= b2 and c1 <= c2
B1 = a1 <= b2 and b1 <= a2 and c1 <= c2
C1 = a1 <= c2 and b1 <= b2 and c1 <= a2
D1 = a1 <= c2 and b1 <= a2 and c1 <= b2
E1 = a1 <= b2 and b1 <= c2 and c1 <= a2
F1 = a1 <= a2 and b1 <= c2 and c1 <= b2
A2 = a1 >= a2 and b1 >= b2 and c1 >= c2
B2 = a1 >= b2 and b1 >= a2 and c1 >= c2
C2 = a1 >= c2 and b1 >= b2 and c1 >= a2
D2 = a1 >= c2 and b1 >= a2 and c1 >= b2
E2 = a1 >= b2 and b1 >= c2 and c1 >= a2
F2 = a1 >= a2 and b1 >= c2 and c1 >= b2
A3 = a1 == a2 and b1 == b2 and c1 == c2
B3 = a1 == b2 and b1 == a2 and c1 == c2
C3 = a1 == c2 and b1 == b2 and c1 == a2
D3 = a1 == c2 and b1 == a2 and c1 == b2
E3 = a1 == b2 and b1 == c2 and c1 == a2
F3 = a1 == a2 and b1 == c2 and c1 == b2
if A3 or B3 or C3 or D3 or E3 or F3:
    answer = 'Boxes are equal'
elif A1 or B1 or C1 or D1 or E1 or F1:
    answer = 'The first box is smaller than the second one'
elif A2 or B2 or C2 or D2 or E2 or F2:
    answer = 'The first box is larger than the second one'
else:
    answer = 'Boxes are incomparable'
print(answer)
