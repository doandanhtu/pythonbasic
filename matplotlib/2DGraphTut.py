import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,2)

func = np.poly1d(np.array([8,-14,-9,11,-1]).astype(float))

plt.plot(x, func(x))
plt.show()



