string = str(input())
a = string.find('f')
b = string.rfind('f')
if a != 0 and b != 0:
    if a == b:
        print(a)
    else:
        print(a, b)
else:
    print()
