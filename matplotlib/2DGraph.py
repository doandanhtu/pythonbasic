'''from pylab import *
x_numbers = [1,2,3,4,5,6,7]
y_numbers = [2,4,5,7,9,10,6]

plot(x_numbers,y_numbers)
show()

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp)
show()'''

import numpy as np
import matplotlib.pyplot as plt

'''
x = np.linspace(0,10)
line = plt.plot(x, np.sin(x) + np.cos(x))
plt.show()

x = np.linspace(-6,6)

#x^2 + 2x + 1

func = np.poly1d(np.array([1,2,1]).astype(float))

plt.plot(x, func(x))
plt.show()'''

import csv
days = []
temp = []
with open('/Users/tudoan/Documents/Programming/PythonBasic/Matplotlib Lecture/nhietdo.csv',newline='') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        days.append(int(row[0]))
        temp.append(float(row[1]))

plt.plot(days, temp)
plt.show()
