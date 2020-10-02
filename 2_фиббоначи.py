fib1 = 1
fib2 = 1
n = int(input())
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    if n == fib2:
        print(n)
    else:
        print(-1)
