def add(x, y):
    return x+y

print(add(4,5))
print(add('Tom','Jerry'))

add = lambda x,y: x + y

print(add(4,5))
print(add('Tom','Jerry'))

def square(x):
    return x ** 2

print(square(8))

g = lambda x: x ** 2

print(g(8))

#lambda & map
print(list(map(g,[1,2,3,4])))

print(list(map(square, [1,2,3,4])))

#lambda & filter

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: x % 3 ==0, foo)))

#reduce: sum elements in a list!
import functools as ft
print(ft.reduce(lambda x,y: x+y, foo))

print(sum(foo))

def add(x,y):
    return x+y

print(ft.reduce(add,foo))

#recursive lambda:

fact = lambda x: fact(x-1)*x if x > 1 else 1
print(fact(3))

#implement a lambda in a function:
def edit_word(words, func):
    for word in words:
        yield func(word)
        #using yield instead of return since we want all words to be executed
        #using return would lead to only the first word is executed!

result = list(edit_word("Hello World", lambda x: x.upper()))
print(''.join(result))

wordLen = []
for word in 'It is raining cats and dogs'.split():
    wordLen.append(len(word))

print(wordLen)

print(list(map(lambda x: len(x), 'It is raining cats and dogs'.split())))

print(list(map(len, 'It is raining cats and dogs'.split())))

