import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''
#points
x = [1, 3, 5, 7, 2, -1, -5, 0, 1, -9]
y = [5, 6, -4, 12, 6, -1, 2, 10, 1, 1]
z = [1, 4, 5, -10, 4, 7, 9, 2, -11, -2]

ax.plot(x, y, z, 'o') ###
plt.show()

#lines

t = np.linspace(0, 10)
x = 2 + 3*t
y = -1 + 2*t
z = t

ax.plot(x, y, z)
plt.show()

#surface
x = np.linspace(-5, 5)
y = np.linspace(-5, 5)
X, Y = np.meshgrid(x, y)
Z = (2*X + 3*Y - 5)/4


ax.plot_surface(X, Y, Z)
plt.show()'''

#sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z)
plt.show()