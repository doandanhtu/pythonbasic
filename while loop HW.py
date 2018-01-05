'''#finding the gcd
int1 = int(input("Enter first integer:"))
int2 = int(input('Enter second integer:'))

gcd = 1
i = 1
while i <= min(int1, int2):
    if int1 % i == 0:
        if int2 % i == 0:
            gcd = i
    i += 1
print('the greatest common division of ', int1, ' and ', int2, ' is ', gcd)
'''



number = int(input('Input an odd number:'))
if number % 2 == 0:
    print('Sorry, the number you enter is an even number.')
else:
    i = number
    numlist = []
    for i in range(number,0,-2):
        for j in range(1, i + 1):
            numlist.append(str(i))
        print(''.join(numlist).center(number))
        numlist = []


    '''for i in range(1,number+2,2):
        for j in range(1,i+2,2):
            print(i,end="")
        print("")

for i in range(7,0,-2):
    print(i)'''

