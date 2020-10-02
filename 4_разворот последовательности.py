def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)
    else:
        print(0)


reverse()
