import collections
f = open('HowLongLyrics.txt', 'r')
content = f.read() #content is now a string
words = content.split() #convert it into a list of words

'''
for word in words:
    print('{0}: {1}'.format(word,words.count(word)))
'''

print(collections.Counter(words))
