'''seasons = ['Spring','Summer','Fall','Winter']
enumerate(seasons)
list(enumerate(seasons))

print(list(enumerate(seasons, start=2)))

skills = ("C++", "Python", "Java", "Objective-C")


print(list(enumerate(skills)))
print(set(enumerate(skills)))
print(dict(enumerate(skills)))'''

x = [1, 5, 7, 3, 8]

for i, j in enumerate(x):
    print('x[%1d] = %1d' %(i,j))