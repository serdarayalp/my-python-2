# Absolute Value Program
# Function to generate the absolute value of a number
def absoluteValue(valueIn):
    if valueIn >= 0 :
        valueOut = valueIn
    else: #must be negative, multiply by minus one to get a positive value
        valueOut = -1 * valueIn
    return valueOut

#Test cases
result = absoluteValue(10.5)
print 'The absolute value of 10.5 is', result

result = absoluteValue(-8)
print 'The absolute value of -8 is', result

userNumber = raw_input('Enter a number: ')
userNumber = float(userNumber)
result = absoluteValue(userNumber)
print 'The absolute value of', userNumber, 'is', result
