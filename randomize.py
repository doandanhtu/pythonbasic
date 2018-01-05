import random as rd
'''rd.SystemRandom()
rd.random()
rd.random() * 10
rd.randrange(0,20,2)

rd.uniform(8,20)

rd.triangular(0,10,1)
rd.choice([1,3,4,6,7,9,-23,34,-67])

rd.choice(['red', 'green', 'blue', 'yellow', 'white', 'black'])

items = [1,2,3,4,5,6,7,8]
rd.shuffle(items)

rd.choice('abcdefghij')

rd.sample([1, 2, 3, 4, 5],  3)

weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
print(population)
print(rd.choice(population))'''

GK = [1,13]
DF = [2,3,14,18,19,22,23,25]
MF = [4,5,6,7,8,12,15,20,21]
FW = [9,10,11,16,17]

team = [GK, DF, MF, FW]
for pos in team:
    if pos == GK:
        gk = rd.sample(GK,1)
        print('goal keeper is number ', gk)
    elif pos == DF:
        df = rd.sample(DF,4)
        print('defenders are number', df[0], df[1], df[2], 'and', df[3])
    elif pos == MF:
        mf = rd.sample(MF,4)
        print('midfielders are number', mf[0], mf[1], mf[2], 'and', mf[3])
    else:
        fw = rd.sample(FW,2)
        print('Attackers will be number', fw[0], 'and', fw[1])
