
'''#str, list and tuple support indexing while set does not
st = "Techmaster VietNam"
A = {1,2,3,4,5,6}

#number, tuple and str are immutable while list and set are mutable
#change by using assignment, append() or extend()

dic = {'dog':'cho','cat':'meo','pig':'heo'}

dic.items()
dic.keys()
dic.values()

dic['dog']


dic['dog'] = 'cun'''


key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}




a = list(input('your message:'))

a1 = []
for char in a:
    for k in key.keys():
        if char == k:
            a1.append(key[char])
            break
    else:
        a1.append(char)

a2 = ''.join(a1)

print(a2)



