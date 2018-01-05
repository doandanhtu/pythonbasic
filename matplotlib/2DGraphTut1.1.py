import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,4)

def y(x):
    return (x**2 + x - 6)/(x**2 - 4)


'''
def y(x):
    return (x + 3)/(x + 2)'''

plt.ylim(0,4)
plt.xlim(-2,4)
plt.grid(True)
plt.plot(x, y(x))


plt.show()
