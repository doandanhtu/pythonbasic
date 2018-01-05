def fib(n: int):
    if n == 0:
        return print('wrong index')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))