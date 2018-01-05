def getUniqueList(inList: list) -> list:
    uniqueList = []
    for item in inList:
        if uniqueList.count(item) == 0:
            uniqueList.append(item)

    return uniqueList

words = ['money', 'love', 'gals', 'power', 'properties', 'money', 'gals', 'wine','friends','power','money','love']

print(getUniqueList(words))