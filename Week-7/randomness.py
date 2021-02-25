from random import randrange
# from random import random


def getGuess():
    return int(input('Enter your guess from 1 to 100: '))


def main():
    print('Welcome to the guessing game')
    print('I have chosen a number from 1 to 100')
    print('You have seven guesses to find it. Good luck!')
    print()

    secretNumber = randrange(0, 100) + 1
    guess = getGuess()
    guesses = 1

    while (guess != secretNumber and guesses < 7):
        guess = getGuess()
        guesses += 1

    if guesses < 7:
        print('You got it!')
    else:
        print('You did not guess it! The number was {}'.format(secretNumber))


main()
