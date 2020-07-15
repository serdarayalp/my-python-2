def printText(param1):
    print param1
    separateRuns() # call another function

def separateRuns():
    print '*********************************'
    print

def addTwo(startingValue):
    endingValue = startingValue + 2
    return endingValue

def calculateAverage(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4

    # Divide by a floating point value to ensure we get the proper potentially fractional answer
    average = total / 4
    
    print 'Average value is:', average

def square(number):
    answer = number * number
    return answer


userNumber = raw_input('Enter a number: ')
userNumber = float(userNumber) # convert to a float
numberSquared = square(userNumber) # call the function and save the result
print 'The square of your number is: ', numberSquared

    
#calculateAverage(2, 3, 4, 5)
#calculateAverage(-3, 5.2, 15, 1000.8)
#calculateAverage(1.4, -2.5, 14.3, 200.5)

# Call the function twice with different arguments
# sum1 = addTwo(5)
# print "Das Ergebnis is: ", sum1
# addTwo(10)

# main code starts here
# printText('Das ist ein Test 1')
# printText('Das ist ein Test 2')
