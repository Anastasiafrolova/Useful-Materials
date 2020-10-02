string = str(input())
a = string.find('h')
b = string.rfind('h')
string_new = string[a+1:b]
print(string[:a+1], string_new.replace('h', 'H'), string[b:], sep='')
