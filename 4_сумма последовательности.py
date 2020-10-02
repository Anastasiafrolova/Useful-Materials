i = 0


def summa():
    global i
    n = int(input())
    if n != 0:
        i += n
        summa()
    elif n == 0:
        print(i)


summa()
