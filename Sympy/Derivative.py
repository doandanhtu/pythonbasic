from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', int = True)
f, g, h = symbols('f g h', cls = Function)
init_printing(use_unicode=True)
diff(x**2 + 2*x,x)
diff(x**5+5*x**4+3*x**2+2*x,x,x,x)
diff(x**5+5*x**4+3*x**2+2*x,x,3)

diff(x**5+y**4*x**2+z**3*x**4+t*x, x)
diff(x**5+y**4*x**2+z**3*x**4+t*x, x, y)
diff(x**5+y**4*x**2+z**3*x**4+t*x, x, y, z)

f = Derivative(x**5+y**4*x**2+z**3*x**4+t*x, x)
f
f.doit()
print(f)


