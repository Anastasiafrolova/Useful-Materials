string = str(input())
a = string.find('f')
b = string.rfind('f')
if a == -1 and b == -1:
    print()
else:
    if a == b:
        print(a)
    else:
        print(a, b)
