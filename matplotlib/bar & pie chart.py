import matplotlib.pyplot as plt

'''
x1Values = [1,3,5,7,9]
y1Values = [4,5,8,7,12]
plt.bar(x1Values, y1Values, width=0.2, label='bar1', color = 'red')

x2Values = [2,4,6,8,10]
y2Values = [2,3,4,5,10]
plt.bar(x2Values, y2Values, width=0.2, label='bar2', color = 'black')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar chart example \n Hope you enjoy!!')
plt.legend()
plt.show()'''

mobileBranches = ['Apple', 'SamSung', 'Nokia', 'BlackBerry']
slices = [30, 30, 20, 20]
colors = ['red', 'blue', 'yellow', 'purple']
explode = [0.1, 0, 0, 0]
plt.pie(slices, labels = mobileBranches, colors = colors, startangle= 0, explode = explode, autopct='%1.1f%%' )
plt.show()

plt.pie()