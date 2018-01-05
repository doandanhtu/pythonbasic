import random
class People:
    def __init__(self, eyeColor, skinColor, hairColor):
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = hairColor

class EuropeanPeople(People):
    def __init__(self, country):
        People.__init__(self, 'blue', 'white', 'blond')
        self.country = country

    def goodAtArtSport(self):
        print('%s is good at Art and Sport' % self.country)

    def __str__(self):
        return '%s person has %s eyes, %s skin and %s hair' % (self.country, self.eyeColor, self.skinColor, self.hairColor)

class AsianPeople(People):
    def __init__(self, country):
        People.__init__(self, 'black', 'yellow', 'black')
        self.country = country

    def goodAtMath(self):
        print('%s is good at Math' % self.country)

    def __str__(self):
        return '%s person has %s eyes, %s skin and %s hair' % (self.country, self.eyeColor, self.skinColor, self.hairColor)

swedishPeople = EuropeanPeople('Swedish')
print(swedishPeople)

print()

japanesePeople = AsianPeople('Japanese')
print(japanesePeople)

class EuroAsiaPeople(EuropeanPeople, AsianPeople):
    def __init__(self, motherCountry, fatherCountry):
        self.country = '%s - %s' % (motherCountry, fatherCountry)
        self.eyeColor = random.choice(['blue', 'black', 'dark blue'])
        self.skinColor = random.choice(['white', 'yellow', 'pink'])
        self.hairColor = random.choice(['blond','black','red'])

    def __str__(self):
        return '%s person has %s eyes, %s skin and %s hair' % (self.country, self.eyeColor, self.skinColor, self.hairColor)

japaneseSweden = EuroAsiaPeople('Swedish','Japanese')
print(japaneseSweden)

japaneseSweden.goodAtArtSport()
japaneseSweden.goodAtMath()
print(type(japaneseSweden).__name__)
print(japaneseSweden.__class__.__name__)
print(japaneseSweden.__class__.__base__.__name__) #the mother class only
print(japaneseSweden.__class__.__base__)
print(japaneseSweden.__class__.__bases__)
print(japaneseSweden.__class__.__bases__[0].__name__)
print(japaneseSweden.__class__.__bases__[1].__name__)

#HW
class Car:
    def __init__(self):
        pass

    def viableOnRoad(self):
        print('%s is viable on road' % self.__class__.__name__)

class Canoe:
    def __init__(self):
        pass
    def viableOnWater(self):
        print('%s is viable on water' % self.__class__.__name__)

class AmphibiousVehicle(Car, Canoe):
    def __init__(self):
        pass

car = Car()
canoe = Canoe()
amp = AmphibiousVehicle()
car.viableOnRoad()
canoe.viableOnWater()
amp.viableOnRoad()
amp.viableOnWater()

'''class Car:
    def __init__(self, name):
        self.name = name

    def viableOnRoad(self):

        print('%s is viable on road' % self.name)

class Canoe:
    def __init__(self, name):
        self.name = name
    def viableOnWater(self):
        print('%s is viable on water' % self.name)

class AmphibiousVehicle(Car, Canoe):
    def __init__(self, motherName, fatherName):
        self.name = 'Amp of %s and %s' %(motherName, fatherName)

car = Car('hunter')
canoe = Canoe('shark')
amp = AmphibiousVehicle('hunter','shark')
car.viableOnRoad()
canoe.viableOnWater()
amp.viableOnRoad()
amp.viableOnWater()'''