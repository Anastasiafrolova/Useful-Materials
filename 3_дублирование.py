s = str(input())
a = s.find('h')
b = s.rfind('h')
print(s[0:b], s[a+1:], sep='')
