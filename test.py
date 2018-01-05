'''name = "Tu"
age = 23
print("My name is", name, ". I am ", age)

print("My name is %s. I am %d" % (name, age))

#Format print
primeNum = [1, 2, 3, 5, 7, 11, 13, 17, 19]
i = 0
for prime in primeNum:
    print('%2d: %2d' % (i, prime))
    i += 1

#Following example taken from https://docs.python.org/3/tutorial/inputoutput.html
#print without newline
for prime in primeNum:
    print("%2d, " % prime, end='')

for x in range(1,11):
    print('{0:4d} {1:4d} {2:4d}'.format(x,x*x,x*x*x))

print('We are the {} who say {}'.format('knights','Ni'))
print('{0} and {1}'.format("eggs", "spams"))
print('{1} and {0}'.format("eggs", "spams"))
print('This {food} is {adjective}'.format(food='spam',adjective='horrible'))
print('the story of {0}, {1} and {other}'.format('Bill','Manfred',other='Georg'))
print('the story of {1}, {0} and {other}'.format('Bill','Manfred',other='Georg'))

import math
print('the value of pi is approximately {0:.8f}'.format(math.pi))

pi

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

dic = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(dic))

canfly = True
canswim = True
canchasemouse = True

if canfly:
    if canswim:
        print("duck")
    elif canchasemouse:
        print('Eagle')
    else:
        print('Bird')
else:
    print('chicken')

for i in range(0,10):
    if i % 2 == 0:
        print(i,' is even')


#conditional syntax
score = 74
if score >= 90:
    print('grade is A')
elif score >= 80:
    print('grade is B')
elif score >= 70:
    print('grade is C')
elif score >= 60:
    print('grade is D')
else:
    print('grade is F')

w = 145.5
h = 66.14

weight = w*0.45359237
height = h*0.0254
BMI = weight / (height*height)

if BMI < 18.5:
    print('underweight')
elif BMI <25:
    print('Normal')
elif BMI <30:
    print('Overweight')
else:
    print('obese')

#comparison
name = 'abc'
#name2 = 'a' + 'b' + 'c'
#name2 = ''.join(['a','b','c'])
name2 = 'ABC'.lower()

print(name2)

if name == name2:
    print('equal')
else:
    print('not equal')

if name is name2:
    print('identical')
else:
    print('not identical')

print(id(name),id(name2))

if name is not name2:
    print('name is not name2')

if not (name is name2):
    print('name is not name2')

x = 2/7
print(x)
y = 0.28571428571428573
print(y)

if x is y:
    print('x is y')
else:
    print('x is not y')

if x == y:
    print('x is equal to y')
else:
    print('x is not equal to y')

if abs(x - y) < 0.0000001:
    print('x is similar to y')
else:
    print('x and y are different')

#for loop
import sys
from termcolor import colored, cprint

tasks = ['Get Requirements','Design','Code','Test','Ship','Fix Bug']
for task in tasks:
    print(task)

for i in range(len(tasks)):
    print('task %d %s' % (i,tasks[i]))

name = 'Jame Cook'
for char in name:
    print(char)

numbers = [12, 16, 17, 24, 29, 30]
for i in numbers:
    if i % 2 == 1:
        continue
    print(i)
print('done')

for num in range(1, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num,i,j))
            break
    else:
        #print(num, 'is a prime number')
        cprint(str(num) + ' is a prime number', 'red', 'on_yellow')

for i in range(10, -11, -1):
    print(i)

i = 0
while i < 100:
    print(i)
    i += 5

#Nested for loop
for i in range(1, 10):
    print('-----------')
    for j in range(1, 10):
        print('%2d *%2d = %2d' % (i,j,i*j))

students = [("Alejandro", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for name, subjects in students:
    print(name, 'takes', len(subjects), 'courses')

counter = 0
for name, subjects in students:
    for s in subjects:
        if s == "CompSci":
            counter += 1

print('The number of students taking CompSci is',counter)


#Multiplication table
print('          Multiplication Table')
for i in range(1, 10):
    if i == 1:
        print('%1s ' % '','%4d' % i, end='')
    else:
        print('%4d' % i, end='')
print("")
print('---------------------------------------')
for i in range(1, 10):
    print(i, '|', end='')
    for j in range(1, 10):
        print('%4d' % (j*i), end='')
    print("")

#while loop
correctNum = 77

while True:
    number = int(input("Guess a number between 0 and 100:"))
    if number == correctNum:
        print('Yes')
        break
    elif number > correctNum:
        print('the correct number is lower than your guess')
    else:
        print('the correct number is higher than your guess')
'''

NoOfPrimes = int(input("Number of primes you would like to show:"))
NoOfPrimesPerLine = int(input("Number of primes displayed per line:"))

CountOfPrimes = 0
CountOfPrimesPerLine = 0

i = 1
while CountOfPrimes < NoOfPrimes:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        CountOfPrimes += 1
        print('%6d' % i, end="")
        CountOfPrimesPerLine += 1
        if CountOfPrimesPerLine >= NoOfPrimesPerLine:
            print("")
            CountOfPrimesPerLine = 0
    i += 1



