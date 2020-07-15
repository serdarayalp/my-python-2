# Allow the program to use random numbers
import random

while True:
    
    # prints a blank line
    print

    # raw_input() = Eingabe wir als String verabeitet (Python2)
    # input() = Eingabe wird evaluiert (Python2)
    # input() = Eingabe wir als String verabeitet (Python3)
    # eval(input()) = Eingabe wird evaluiert (Python3)
    usersQuestion = raw_input('stelle eine Ja/Nein-Frage (RETURN, um die Applikation zu beenden): ')
    
    if usersQuestion == '':
        break

    # pick a random number
    randomAnswer = random.randrange(8)
    
    if randomAnswer == 0:
        print 'It is certain.'
    elif randomAnswer == 1:
        print 'Absolutely!'
    elif randomAnswer == 2:
        print 'You may rely on it.'
    elif randomAnswer == 3:
        print 'Answer is foggy, ask again later.'
    elif randomAnswer == 4:
        print 'Concentrate and ask again.'
    elif randomAnswer == 5:
        print 'Unsure at this point, try again.'
    elif randomAnswer == 6:
        print 'No way, dude!'
    elif randomAnswer == 7:
        print 'No, no, no, no, no.'
