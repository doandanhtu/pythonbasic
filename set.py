a = set('abracadabra')
print(a)

skillA = {'C++','Python','Java','JavaScript'}

skillB = {'Photoshop', 'JavaScript', 'CSS', 'Java'}

print(skillA - skillB) #A but not B
print(skillB - skillA) #B but not A
print(skillA | skillB) #union
print(skillA & skillB) #intersection

list(skillA & skillB)
list(skillA | skillB)

skillX = set(['Cook', 'Dance'])

type(skillX)

sharedskills = skillA.intersection(skillB)

allskills = skillA.union(skillB)

skillA ^ skillB

skillA.difference(skillB) #=skillA - skillB

skillC = {'C++', 'Python'}

skillC.issubset(skillA)

skillA.issuperset(skillC)

skillB.add('Bootstrap')

skillA.isdisjoint(skillB)

skillA.isdisjoint(skillX)


