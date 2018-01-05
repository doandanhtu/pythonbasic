class People:
    def __init__(self, eyeColor, skinColor, hairColor):
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = hairColor

class EuropeanPeople():
    def __init__(self, country):
        self.country = country
        self.people = People('blue', 'white', 'blond')

    def goodAtArtSport(self):
        print('%s is good at Art and Sport' % self.country)

    def __str__(self):
        return '%s person has %s eyes, %s skin and %s hair' % (self.country, self.people.eyeColor, self.people.skinColor, self.people.hairColor)

class AsianPeople():
    def __init__(self, country):
        self.country = country
        self.people = People('black', 'yellow', 'black')

    def goodAtMath(self):
        print('%s is good at Math' % self.country)

    def __str__(self):
        return '%s person has %s eyes, %s skin and %s hair' % (self.country, self.people.eyeColor, self.people.skinColor, self.people.hairColor)

swedishPeople = EuropeanPeople('Swedish')
print(swedishPeople)

print()

japanesePeople = AsianPeople('Japanese')
print(japanesePeople)

class addsub():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return  self.x - self.y

class multidivide():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multi(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

class calc():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.addsub = addsub(x, y)
        self.multidivide = multidivide(x, y)

    def add(self):
        return self.addsub.add()
    def sub(self):
        return self.addsub.sub()
    def multi(self):
        return self.multidivide.multi()
    def divide(self):
        return self.multidivide.divide()
    def power(self):
        return self.x ** self.y

Calc = calc(10, 5)
print(Calc.add(),Calc.sub(),Calc.multi(),Calc.divide(),Calc.power())
