#Tut1
'''l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

l2new = reversed(l2)

t = list(zip(l1, l2new))
print(t)'''

list = [1, 3, 4, 6]
t = ('Java', 'Python', 'C++')

t2 = 'Objective-C', 'Swift', 'Ruby'

tnum = tuple([1,2,3,4,5,6])

min(tnum)
max(tnum)

u = (t, t2)

t3 = t + t2

list[0] = 10
len(t3)

p1, p2, p3 = t
print(p1, p2, p3)

t.index('C++')

t3[:3]

list(zip(t,t2))

#Tut2
numList = [9, 3, 2, 5, 6, 8, 11]

numList1 = []
for i in numList:
    if i <= 5:
        numList1.append(i)
numList1.sort()

numList2 = []
for i in numList:
    if i > 5:
        numList2.append(i)
numList2.sort()