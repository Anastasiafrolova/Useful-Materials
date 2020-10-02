def xor(x, y):
    if x == y:
        return False
    else:
        return True


x = int(input())
y = int(input())
if xor(x, y) is True:
    print('1')
if xor(x, y) is False:
    print('0')
