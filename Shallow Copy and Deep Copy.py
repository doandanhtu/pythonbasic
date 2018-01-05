'''a = 10
b = a
a = 20
print(a)
print(b)

lst1 = [1,2,3]
lst2 = lst1
lst1[0] = 100

print(lst1)
print(lst2)'''

list1 = [1,2,3,[4,5]]
import copy

list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)

print(list1,list2,list3,list4)
print(id(list4))
print(id(list3))
print(id(list2))
print(id(list1))

#list1 and list2 have the same id --> they share the same area on the memory

list1[0] = 1000

id(list1),id(list2),id(list3),id(list4)
print(list1,list2,list3,list4)

list1[3][0] = 400
id(list1[3]),id(list2[3]),id(list3[3]),id(list4[3])

listX = list1[:]
