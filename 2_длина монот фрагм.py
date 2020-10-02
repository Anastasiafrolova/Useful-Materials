max_len = 0
temp_len = 1
a = int(input())
while a:
    b = int(input())
    if a == b:
        temp_len += 1
    else:
        if temp_len > max_len:
            max_len = temp_len
            temp_len = 1
    a = b
print(max_len)
