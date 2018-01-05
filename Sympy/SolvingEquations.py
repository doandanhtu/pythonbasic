from __future__ import division
import sympy as sp

x, y, z, t = sp.symbols('x y z t')

sp.solve(x**2 - 1)
sp.solve(x**3 +2*x**2 -x + 1)
sp.solve((x + 5*y - 2, -3*x + 6*y - 15), x, y)

sp.solve((x+y+z,y+1,z-2),x,y,z)

sp.solve(x**3 + 3*x**2 + 2*x + 1)

sp.solve(sp.sin(x)+ sp.cos(x) - 0.5)

sp.solve(sp.sin(x)+ sp.cos(x) - 1)

sp.solve_linear(x + y**2)

sp.solve_linear(1/x - y**2)
