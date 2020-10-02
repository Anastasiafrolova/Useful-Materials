x = int(input())
y = int(input())
z = int(input())
if x >= y >= z or x >= z >= y:
    answer = x
if y >= x >= z or y >= z >= x:
    answer = y
if z >= x >= y or z >= y >= x:
    answer = z
print(answer)
