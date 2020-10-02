now = int(input())
n = 1
sumSeq = now
while now != 0:
    now = int(input())
    sumSeq = sumSeq + now
    average = sumSeq / n
    n = n + 1
print(average)
