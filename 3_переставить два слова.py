s = str(input())
a = s.find(' ')
print(s[a+1:], s[:a], sep=' ')
