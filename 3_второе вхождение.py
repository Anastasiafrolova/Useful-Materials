s = str(input())
a = s.find('f')
s_new = s[:a] + s[a+1:]
print(s_new)
b = s_new.find('f')
if b != -1 and a != -1:
    print(b+1)
elif b == -1:
    if a != -1:
        print(-1)
    elif a == -1:
        print('-2')
