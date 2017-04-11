import random

NUMBER_OF_GUESSES = 10
RANGE_TOP = 10
RANGE_BOTTOM = 0
"""
Uppercase is used to denote these variables are constants
"""

while True:
    # generate the random number between 0 and RANGE (RANGE=10)
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    # raw_input in a for loop gives the user a certain amount of guesses (10 in this case)
    for i in range(NUMBER_OF_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'well done'
            break
        elif guess > random_number:
            print "too high"
            print "guesses remaining:"
            print RANGE_TOP - i
        else:
            print "too low"
            print "guesses remaining:"
            print RANGE_TOP - i

    print "let's try a new number!"
    print "RANGE:"
    print RANGE_TOP
