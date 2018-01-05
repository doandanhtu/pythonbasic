from __future__ import division
import sympy

x, y, z, t = sympy.symbols('x y z t')
k, m, n = sympy.symbols('k m n', integer=True)
f, g, h = sympy.symbols('f g h', cls=sympy.Function)

print(sympy.simplify((x - 1)*(x+1)))
print(sympy.simplify(sympy.sin(x)*sympy.cos(x)))

print(sympy.expand((x+1)**10))

((x + y)*(x - y)).expand(basic=True)
((x+y)**3).expand(basic=True)

sympy.solve(2*x - 1, x)
sympy.solve(x**2 - 1, x)
sympy.solve(x**3 + 1, x)

sympy.simplify(sympy.cos(x)*sympy.cos(y)-sympy.sin(x)*sympy.sin(y))


((x+y)**3).expand(basic=True)