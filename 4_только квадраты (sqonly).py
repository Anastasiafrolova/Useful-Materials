def sqonly(some_flag=False):
    x = int(input())
    if x != 0:
        if sqonly(some_flag):
            some_flag = True
        if x ** 0.5 % 1 == 0:
            print(x, ' ', end='')
            some_flag = True
    return some_flag


if sqonly() is False:
    print('0')
