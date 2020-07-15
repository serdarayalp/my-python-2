def getIntegerFromUser(prompt):
    while True:
        number = raw_input(prompt)
        try:
            number = int(number)
            break
        except:
            print 'That is not an integer, please try again.'
            continue
    return number

def getFloatFromUser(prompt):
    while True:
        number = raw_input(prompt)
        try:
            number = float(number)
            break
        except:
            print 'That is not a float, please try again.'
            continue

    return number

myInteger = getIntegerFromUser('Please enter an integer: ')
print myInteger

myFloat = getFloatFromUser('Please enter a float: ')
print myFloat
