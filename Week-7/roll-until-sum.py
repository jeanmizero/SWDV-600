from random import random


def target_sum():
    return int(input('Enter the target sum to roll for: '))


def main():
    print('This program rolls two 6-sided dice until their sum is a given target value')

    target = target_sum()
    print()

    if(target <= 1 or target >= 13):
        print("Invalid target")
    else:
        rolls = 0

        while True:
            rolls += 1
            roll_number1 = (int(random() * 10)) % 6 + 1
            roll_number2 = (int(random() * 10)) % 6 + 1
            total = roll_number1 + roll_number2

            print('Roll : {0} and {1}, sum is {2}'.format(
                roll_number1, roll_number2, total))

            if(total == target):
                break

        print("Got it in {0} rolls!".format(rolls))


main()
