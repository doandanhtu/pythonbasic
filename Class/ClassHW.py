import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def setRadius(self, newRadius):
        self.radius = newRadius
        return self.radius

circle1 = Circle(10)

print(circle1.getArea())
print(circle1.getPerimeter())
print(circle1.setRadius(15))

class BMI:
    def __init__(self, name, weight, height, age = 20 ):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def getBMI(self):
        return self.weight / (self.height ** 2)

    def getStatus(self):
        if self.getBMI() < 18.5:
            return 'Underweight'
        elif self.getBMI() < 25:
            return 'Normal'
        elif self.getBMI() < 30:
            return 'Overweight'
        else:
            return 'Obese'

    def resultDisplay(self):
        return print('The BMI for', self.name, ' is ', self.getBMI(), ' which is ', self.getStatus())

bmi1 = BMI('Tu',60,1.68,age=23)
bmi2 = BMI('Yami', 66, 1.71)

bmi1.resultDisplay()
bmi2.resultDisplay()