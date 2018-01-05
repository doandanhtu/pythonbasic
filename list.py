fruits = ['Apple', 'Tomato', 'Lemon', 'Kiwi', 'Banana', 'Guava']

fruits[0]

fruits[-1]

fruits[0:3]

fruits[0:6:2]

fruits.append('pine apple')

fruits.sort()

otherfruits = ['Tao', 'Le', 'Cam', 'Chanh']

allfruits = fruits + otherfruits


list(filter(lambda x: x[0] == 'T',allfruits))

words = ['money', 'love', 'gals', 'power', 'properties', 'money', 'gals', 'wine','friends','power','money','love']


uniquewords =[]
for word in words:
    if uniquewords.count(word) == 0:
        uniquewords.append(word)

