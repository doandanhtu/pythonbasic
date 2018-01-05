#1 gcd
#Euclidean Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(1071,462))


#pascal triangle:
def pastri(x: int): #x is the number of rows
    ele = lambda a, b: 1 if b in (0, a) else ele(a - 1, b - 1) + ele(a - 1, b)
    #ele is a lambda func to find the b-th element of row a
    lastlst = []
    for k in range(x + 1):
        lastlst.append(str(ele(x, k)))
    a = '  '.join(lastlst)
    #get the last row for displaying purpose
    for i in range(x):
        lst = []
        for k in range(i +1):
            lst.append(str(ele(i, k)))
            #convert ele from int to str to use join and center
        print('  '.join(lst).center(len(a)))
        print()

pastri(6)
