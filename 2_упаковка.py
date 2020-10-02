l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
number2 = (lc >= l1 + l2) and (wc >= w1) and (wc >= w2)
number3 = (lc >= l1 + w2) and (wc >= w1) and (wc >= l2)
number4 = (lc >= w1 + w2) and (wc >= l1) and (wc >= l2)
number5 = (lc >= w1 + l2) and (wc >= w2) and (wc >= l1)
number6 = (wc >= l1 + l2) and (lc >= w1) and (lc >= w2)
number7 = (wc >= l1 + w2) and (lc >= w1) and (lc >= l2)
number8 = (wc >= w1 + w2) and (lc >= l1) and (lc >= l2)
number9 = (wc >= w1 + l2) and (lc >= w2) and (lc >= l1)
number0 = (lc >= l1) and (wc >= w1)
number11 = (lc >= l2) and (wc >= w2)
number12 = (lc >= w1) and (wc >= l1)
number13 = (lc >= w2) and (wc >= l2)
if (hc < h1) or (hc < h2):
    print('NO')
elif (number11 or number13) and (number12 or number13):
    if hc >= (h1 + h2):
        print('YES')
    elif number or number or number4 or number5:
        print('YES')
    elif number6 or number7 or number8 or number9:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
