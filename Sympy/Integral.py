from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', int = True)
f, g, h = symbols('f g h', cls = Function)
init_printing(use_unicode=True)

integrate(x+1,x)

integrate(x+1,(x,0,10))

f = Integral(exp(-x), (x, 0, oo))

g = Integral(exp(-x**2-y**2), (x, 0, oo), (y, 0, oo))

