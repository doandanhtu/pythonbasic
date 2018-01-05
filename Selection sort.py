import random
import time

time_start = time.perf_counter()
numList = []
for i in range(20):
    numList.append(random.randint(1,100))

print(numList)

for i in range(len(numList)-1):
    imin = i
    for j in range(i+1,len(numList)):
        if numList[j] > numList[imin]:
            imin = j

    temp = numList[i]
    numList[i] = numList[imin]
    numList[imin] = temp

print(numList)
time_stop = time.perf_counter()

print(time_stop - time_start)
