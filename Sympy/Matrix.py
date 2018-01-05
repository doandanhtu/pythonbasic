from sympy import *
from sympy import Matrix
init_printing(use_unicode=True)

A = Matrix([[1, 2, -3, 4], [2, -1, 0, 7], [8, -4, 0, 2]]) #byrow

A = Matrix(3, 4, [1, 2, -3, 4, 2, -1, 0, 7, 8, -4, 0, 2]) #similar to R, byrow

B = Matrix(3, 4, [2, 1, -4, 0, 9, 1, 8, -7, 0, 2, 5, -6])

A + B
A - B
A * B

C = Matrix(4, 2, [2, 3, 10, -4, 5, 7, 0, 9])

A * C

D = Matrix([[1, 2, -3], [2, -1, 0], [8, -4, 0]])

D ** 2

D ** 100

