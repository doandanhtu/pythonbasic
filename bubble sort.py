'''import random
numList = []
for index in range(10):
    numList.append(random.randint(1,100))

print(numList)

for i in range(0,len(numList)-1):
    for j in range(i+1,len(numList)):
        if numList[i] > numList[j]:
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp

print(numList)'''

import random, string
length = int(input('place your string\'s length which is 5 and 10:'))
letters = string.ascii_lowercase
randStr = []
if 5 <= length <= 10:
    for i in range(length):
        randStr.append(random.choice(letters))

    print(randStr)
else:
    print('your string\'s length is not in the suitable range')

for i in range(0,length-1):
    for j in range(i+1,length):
        if randStr[i] < randStr[j]:
            temp = randStr[i]
            randStr[i] = randStr[j]
            randStr[j] = temp
print(randStr)
