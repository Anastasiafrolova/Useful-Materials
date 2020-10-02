previous = int(input())
n = 0
while previous != 0:
    next = int(input())
    if next > previous and next != 0:
        n = n + 1
    previous = next
print(n)
