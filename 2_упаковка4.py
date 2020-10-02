l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
if w1 > l1:
    (w1, l1) = (l1, w1)
if w2 > l2:
    (w2, l2) = (l2, w2)
if wc > lc:
    (wc, lc) = (lc, wc)
if h1 > hc or h2 > hc:
    answer = 'NO'
else:
    if l1 > lc or l2 > lc or w1 > wc or w2 > wc:
        answer = 'NO'
    else:
        if h1 + h2 <= hc:
            answer = 'YES'
        elif l1 + l2 <= lc or w1 + w2 <= wc:
            answer = 'YES'
        elif (l1 + w2 <= lc and l2 <= wc) or (l2 + w1 <= lc and l1 <= wc):
            answer = 'YES'
        elif w1 + w2 <= lc and l1 <= wc and l2 <= wc:
            answer = 'YES'
        else:
            answer = 'NO'
print(answer)
