import os

fileHandle = open('my-text-file.txt','r')
data = fileHandle.read()
fileHandle.close()

print data
