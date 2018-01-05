#1
fib = lambda n: fib(n-1)+fib(n-2) if n >=2 else 1
for i in range(10):
    print(i, fib(i))

#2
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
foo1 = list(filter(lambda x: x % 2 == 1, foo))

import functools
print(functools.reduce(lambda x,y: x+y, foo1))

def oddSum(alist: list):
    alist1 = []
    for x in alist:
        if x % 2 == 1:
            alist1.append(x)
    return print(sum(alist1))

oddSum(foo)