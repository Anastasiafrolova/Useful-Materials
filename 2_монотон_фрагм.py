N = int(input())
M = N
(i, j, a, b) = (1, 1, 1, 1)
while N != 0:
    if N > M:
        i += 1
        if i > j:
            j += 1
    else:
        i = 1
    if N < M:
        a += 1
        if a > b:
            b += 1
    else:
        a = 1
    M = N
    N = int(input())
if j > b:
    answer = j
else:
    answer = b
print(answer)
