from FileReadWrite import *

DATA_FILE_PATH = 'my-text-file.txt'

stringToWriteOutToFile = 'Serdar Ayalp'
writeFile(DATA_FILE_PATH, stringToWriteOutToFile)

stringReadInFromFile = readFile(DATA_FILE_PATH)

print 'Read in: ', stringReadInFromFile
