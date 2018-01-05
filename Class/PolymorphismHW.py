class Animal:
    def voice(self):
        pass

class Tiger(Animal):
    def voice(self):
        return print('grrrrr')

class Elephant(Animal):
    def voice(self):
        return print('arggggggg')

class Cat(Animal):
    def voice(self):
        return print('meow')

class Rabbit(Animal):
    def voice(self):
        return print('erkkkkk')

class Dog(Animal):
    def voice(self):
        return print('woofffff')

tigr = Tiger()
el = Elephant()
nyan = Cat()
shia = Rabbit()
wof = Dog()

animals = [tigr, el, nyan, shia, wof]
for animal in animals:
    animal.voice()