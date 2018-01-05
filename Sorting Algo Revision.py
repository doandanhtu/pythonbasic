#create a list of 20 random numbers
import random
import time

numList = []

for i in range(20):
    numList.append(random.randint(1,100))
print(numList)

#selection sort in one loop (using buil-in function 'min')
#if we want to make it descending, using 'max' instead.



import copy
numListClone1 = copy.deepcopy(numList)
newnumList = []
for i in range(0,len(numListClone1)):
    newnumList.append(min(numListClone1[:]))
    numListClone1.remove(min(numListClone1[:]))
print(newnumList)



#selection sort in 2 loops:

numListClone3 = copy.deepcopy(numList)
for i in range(0,len(numListClone3)-1):
    imin = i
    for j in range(i+1,len(numListClone3)):
        if numListClone3[j] < numListClone3[imin]:
            imin = j
    temp = numListClone3[i]
    numListClone3[i] = numListClone3[imin]
    numListClone3[imin] = temp
print(numListClone3)


#bubble sort:

numListClone2 = copy.deepcopy(numList)
for i in range(0,len(numListClone2)-1):
    for j in range(i+1,len(numListClone2)):
        if numListClone2[j] < numListClone2[i]:
            temp = numListClone2[i]
            numListClone2[i] = numListClone2[j]
            numListClone2[j] = temp
print(numListClone2)




#insertion sort with while loop:

numListClone4 = copy.deepcopy(numList)
for i in range(1,len(numListClone4)):
    j = i
    while j > 0:
        if numListClone4[j] < numListClone4[j-1]:
            temp = numListClone4[j]
            numListClone4[j] = numListClone4[j-1]
            numListClone4[j-1] = temp
        j -= 1
print(numListClone4)




#insertion sort with 2 for-loops:

numListClone5 = copy.deepcopy(numList)

for i in range(1,len(numListClone5)):
    for j in range(0,i):
        if numListClone5[i] < numListClone5[j]:
            #numListClone5[j], numListClone5[i] = numListClone5[i], numListClone5[j]
            temp = numListClone5[i]
            numListClone5[i] = numListClone5[j]
            numListClone5[j] = temp
print(numListClone5)




'''instead of:
            temp = numListClone5[i]
            numListClone5[i] = numListClone5[j]
            numListClone5[j] = temp
we can:
numListClone5[j], numListClone5[i] = numListClone5[i], numListClone5[j]
'''

#Quick Sort:

numListClone6 = copy.deepcopy(numList)
def quicksort(alist):
    less = []
    equal = []
    greater = []
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        for x in alist:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return quicksort(less) + equal + quicksort(greater)

print(quicksort(numListClone6))




