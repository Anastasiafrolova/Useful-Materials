x = int(input())
y = int(input())
answer = x == 1 or y - x <= x and (x - 1) % (y - x + 1) == 0
if answer is True:
    total = 'YES'
else:
    total = 'NO'
print(total)
