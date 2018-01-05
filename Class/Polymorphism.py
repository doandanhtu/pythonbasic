import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * (self.radius * 2)

smallRec = Rectangle(10, 20)
circle = Circle(10)

'''print(smallRec.area())
print(smallRec.perimeter())
print(circle.area())
print(circle.perimeter())'''

class Car:
    pass

class BMW(Car):
    pass

car = Car()
bmw = BMW()

shapes = [smallRec, circle, car, bmw]

for shape in shapes:
    print(shape.__class__.__name__)
    if shape.__class__.__base__.__name__ == 'Shape':    #introspection reflection
        print('area',shape.area())
        print('perimeter', shape.perimeter())
        #polymorphism

