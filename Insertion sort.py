import random

numList = []
for i in range(20):
    numList.append(random.randint(1,100))

print(numList)

'''for i in range(1,len(numList)):
    j = i
    while j > 0:
        if numList[j] < numList[j-1]:
            temp = numList[j-1]
            numList[j-1] = numList[j]
            numList[j] = temp
        j -= 1

print(numList)'''

for i in range(0,len(numList)-1):
    for j in range(i+1,len(numList)):
        if numList[i] < numList[j]:
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp

print(numList)