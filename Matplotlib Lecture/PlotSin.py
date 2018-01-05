import numpy as np
import matplotlib.pyplot as plt

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
x = np.linspace(0, 10)
line = plt.plot(x, np.sin(x))


plt.show()