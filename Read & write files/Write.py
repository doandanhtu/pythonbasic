f = open('test.txt', 'r+')

f.write('Line0') #write
f.read()

f.close #save by closing
f = open('test.txt', 'r+')

f = open('test.txt', 'a+')
f.read()
f.seek(0)
f.read()

f.seek(0)
f.write('\r\nLine7')

f = open('test.txt', 'w')
f.read()

f.write('this is a new file')
f.close
f = open('test.txt', 'a+')

f.read()

f.write(' and this is a new content')
f.write('\nthis is a new line')