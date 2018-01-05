class Employee:
    empCount = 0    #class data member, stay outside any methods
    def __init__(self, name, salary):   #constructor special method, first time defining the object
        self.name = name
        self.salary = salary
        self.courses = []
        Employee.empCount += 1

    def displayCount(self): #instance method
        return print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):  #instance method
        return print('Name: ', self.name, ', Salary: ', self.salary)

#these 3 above can only be called via objects
#to call it by class, use @staticmethod:
    @staticmethod
    def employeeCount():    #static method defined by an annotation, this is class method defined within class, not object
        return print('Total Employee %d' % Employee.empCount)

    def enroll(self,course):    #instance method
        self.courses.append(course)

    def showEnrolledCourses(self):  #instance method
        return print(self.courses)

linh = Employee('Linh', 1000)
thang = Employee('Thang', 500)

linh.displayEmployee()
thang.displayEmployee()

linh.displayCount()

cuong = Employee('Cuong', 800)

Employee.employeeCount()

linh.enroll('Math')
linh.enroll('Chemistry')
linh.showEnrolledCourses()