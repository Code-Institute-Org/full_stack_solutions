import random

NUMBER_OF_GUESSES = 10
RANGE_TOP = 10
RANGE_BOTTOM = 0

# Uppercase is used to denote these variables are constants


while True:
    # generate the random number between RANGE_BOTTOM and RANGE_TOP
    # (in this case between RANGE_BOTTOM of 0 and RANGE_TOP of 10)
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    # raw_input in a for loop gives the user a certain amount
    # of guesses (10 in this case)

    for i in range(NUMBER_OF_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'well done'
            break
        elif guess > random_number:
            print "too high"
            print "guesses remaining:"
            print NUMBER_OF_GUESSES - 1 - i
        else:
            print "too low"
            print "guesses remaining:"
            print NUMBER_OF_GUESSES - 1 - i

    print "let's try a new number!"
    print "RANGE TOP:"
    print RANGE_TOP
    print "RANGE BOTTOM:"
    print RANGE_BOTTOM
