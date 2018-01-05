numbers = [1,8,3,5,7,9,11,13,15,17,19]
for i in numbers:
    if i % 2 == 0:
        print('found even')
        break
else:
    print('All are odd numbers')

i = 0
while i <= 10:
    print(i)
    i += 1
else:
    print(i, 'is more than 10')