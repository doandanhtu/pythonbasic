def fibonacci(n: int):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(i, fibonacci(i))

def calculateInterest(amount: int, rate, months: int):
    amountNInterest = amount
    for i in range(months):
        amountNInterest += amountNInterest * rate

    return (amountNInterest, amountNInterest - amount)

print(calculateInterest(1000, 0.01, 10))

import math
import cmath
def quadEquation(a, b, c):
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            return (-b + math.sqrt(delta))/(2*a), (-b - math.sqrt(delta))/(2*a)
        elif delta < 0:
            return complex(-b/(2*a), math.sqrt(-delta)/(2*a)), complex(-b/(2*a), -math.sqrt(-delta)/(2*a))
        else:
            return -b/(2*a)
    else:
        if b != 0:
            return -c/b
        else:
            return None

print(quadEquation(1, 2, 2))