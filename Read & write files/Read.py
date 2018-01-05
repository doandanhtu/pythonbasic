'''
f = open("/Users/tudoan/Downloads/Call Detailed Records.csv", mode='rb')
f.read()'''

f = open("/Users/tudoan/Downloads/Call Detailed Records.csv", 'rb')

f.mode #mode: rb, r, w, a, ...
f.name #file name including path
f.closed #check if file is closed
f.close() #close file
f.closed
f.readline() #read a line
f.tell() #current position

f.readline()

f.seek(0)

f1 = open('test.txt', 'r')

from pandas import *
cdr = read_csv("/Users/tudoan/Downloads/Call Detailed Records.csv")

cdr.count()

