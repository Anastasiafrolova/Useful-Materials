a = int(input())
if a % 10 == 1:
    if a != 11:
        answer = 'korova'
    else:
        answer = 'korov'
if a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    if a != 10 + a % 10:
        answer = 'korovy'
    else:
        answer = 'korov'
if 9 >= a % 10 >= 5:
    answer = 'korov'
print(a, answer)
