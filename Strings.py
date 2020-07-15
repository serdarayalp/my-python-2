# Iterate through a string
# This is the WRONG approach, just showing a concept!

state = 'Mississippi'

myIndex = 0
while myIndex < len(state):
    print state[myIndex]
    myIndex = myIndex + 1

print

for letter in state:
    print letter

sample = 'This is a sample string'
print sample[10:]
print sample[:16]
print sample[:]

startingList = [22, 104, 55, 37, -100, 12, 25]
print startingList[3:6]

