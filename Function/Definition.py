def add(x, y):
    return x + y

print(add(1,3))
print(add('a', 'd'))

def addInt(x: int, y: int) -> int:
    return x+y

print(addInt(1,3))
print(addInt('a', 'd'))

#variadic function:
def avg(first, *rest):
    return (first + sum(rest))/(1+len(rest))

print(avg(1,2,3,4))

'''def a(head, *middle, tail):
    for i in middle:
        print(i)
'''

def a(head, *middle, tail):
    midList = []
    for i in middle:
        midList.append(i)
    return print(midList)

#function parameter with default value:
def calSalpw(paypd, workingdays = 5):
    return paypd * workingdays

print(calSalpw(500))
print(calSalpw(500,6))

#default parameter:
def programmerInfo(name: str, age: int, isMale = True):
    return print('{0} at age {1:2d}. Is male? {2}'.format(name, age, isMale))

print(programmerInfo('Bill',40))
print(programmerInfo('Ada',81,False))

#return more than one value:
def numandneg(x: int):
    #return as tuple: nothing or ()
    #return x, -x
    #return (x, -x)
    return [x, -x]

print(numandneg(10))

import math
def trigonometric(alpha: float) -> float:
    return math.sin(alpha), math.cos(alpha)

print(trigonometric(math.pi * 0.5))

#recursive function:

def factorial(x: int) -> int:
    if x < 2:
        return 1
    else:
        return factorial(x-1) * x

#function that returns function

def bonPhepToan(operator: str, a: int, b: int):
    if operator == "+":
        def add(a, b):
            return a + b
        return add(a, b)

    elif operator == "-":
        def minus(a, b):
            return a - b
        return minus(a, b)

    elif operator == "*":
        def multiply(a, b):
            return a * b
        return multiply(a, b)

    elif operator == "/":
        def divide(a, b):
            return a / b
        return divide(a, b)
    else:
        return print('wrong operator')

