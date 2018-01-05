import time

time_start = time.perf_counter()
i = 1
primeCount = 0
primeList = []
while primeCount < 100:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        primeCount += 1
        primeList.append(i)
    i += 1
print(primeList)

time_stop = time.perf_counter()
print(time_stop - time_start)