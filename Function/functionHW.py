def quadEquaSolver(a: float, b: float, c: float) -> float:
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return None
        else:
            return (-b + delta ** (1/2)) / 2 * a, (-b - delta ** (1/2)) / 2 * a
    else:
        if b != 0:
            return -c / b
        else:
            return None

print(quadEquaSolver(1,2,1))
print(quadEquaSolver(1,1,1))
print(quadEquaSolver(1,3,2))
print(quadEquaSolver(0,2,1))
print(quadEquaSolver(0,0,2))

def deposit(m: float, r: float, n: float) -> float:
    currentBalance = m * ((1 + r) ** n)
    interest = currentBalance - m
    return currentBalance, interest

print(deposit(1000,0.01,10))

