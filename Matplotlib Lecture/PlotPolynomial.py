import numpy as np
import matplotlib.pyplot as plt

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
x = np.linspace(-6, 6)
#x^2 + 2*x + 1

#func = np.poly1d(np.array([1, -2, 1]).astype(float))
func = np.poly1d(np.array([1, -2, 1, 1]).astype(float))
line = plt.plot(x, func(x))

plt.show()