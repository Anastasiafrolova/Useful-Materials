a = int(input())
while a % 10 > 0:
    if a == 0:
        print('0', end='')
    elif a != 0:
        print(a % 10, end='')
    a = a // 10
