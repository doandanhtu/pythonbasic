'''stack = []

stack.append(1)

name = 'Doan Danh Tu'

reversed(name)

print(name[::-1])
'''


'''name = 'Doan Danh Tu'
namelist=[]
for char in name:
    namelist.append(char)
print(namelist)

namelistrever = []

for i in range(len(namelist)):
    namelistrever.append(namelist.pop())
print(namelistrever)

print(''.join(namelistrever))'''



fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']

countFruits = []
diffFruits = []
for fruit in fruits:
    if diffFruits.count(fruit) == 0:
        diffFruits.append(fruit)
for fruit in diffFruits:
    countFruits.append(fruits.count(fruit))

result = list(zip(diffFruits,countFruits))

