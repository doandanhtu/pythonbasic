'''x = [1, 2, 3]
y = [4, 5, 6, 7, 12, 15]

zipped = zip(x,y)

print(list(zipped))

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
drinks = ['coffee', 'tea', 'beer']
fruits = ['banana', 'orange', 'peach']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, drink, fruit, dessert in zip(days, drinks, fruits, desserts):
    print(day, 'drinks', drink, 'eats', fruit, 'enjoys', dessert)
'''

x = [9, 2, 1, 2, 3, 4, 20, 3, 8]
y = [4, 5, 12, 7, 6, 5, 0, 7, 4]

a = len(x)

i = 0
while i < a:
    if (x[i] + y[i] > 10):
        del x[i]
        del y[i]
        a -= 1
        i = 0
    i += 1

print(x)
print(y)

zipped = zip(x,y)
print(list(zipped))


