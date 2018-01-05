cancodeweb = True
cancodemob = False
candesignui = True

boolList = [cancodemob,cancodeweb,candesignui]

if all(boolList):
    print('SuperMan')
elif any(boolList):
    print('Recruitment')
else:
    print('send to TM')

bin(5)

hex(17)

name = 'John'

id(name)

number = [23, 4, 5, 67, 45]

min(number)

max(number)

dir()
len(number)

nums = [-1 , 2, -3, 6]

posnums = map(abs,nums)

list(posnums)

sum(nums)

list(reversed(nums))

import math

round(math.pi, 7)

age = int(input('tell me your age:'))

