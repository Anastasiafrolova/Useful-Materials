a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
A2 = (a1 // a2) * (b1 // b2) * (c1 // c2)
B2 = (a1 // a2) * (c1 // b2) * (b1 // c2)
C2 = (b1 // a2) * (a1 // b2) * (c1 // c2)
D2 = (b1 // a2) * (c1 // b2) * (a1 // c2)
E2 = (c1 // a2) * (a1 // b2) * (b1 // c2)
F2 = (c1 // a2) * (b1 // b2) * (a1 // c2)
if A2 >= B2:
    B2 = A2
if C2 >= D2:
    D2 = C2
if E2 >= F2:
    F2 = E2
if B2 >= D2 and B2 >= F2:
    print(B2)
elif D2 >= F2:
    print(D2)
else:
    print(F2)
