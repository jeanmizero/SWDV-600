def unique_list(item):
    # Empty dictionary
    positive_integer = {}

    for number in item:
        # key in dictionary
        if number in positive_integer:
            return False
        else:
            positive_integer[number] = 1
    return True


def main():
    print("This program tests if the sequence of positive numbers you input are unique")
    print("Enter -1 to quit")

    inputs = int(input("Enter the first number : "))
    # Make empty list
    list_numbers = []

    while inputs != -1:
        list_numbers.append(inputs)
        inputs = int(input("Next : "))

    if unique_list(list_numbers):
        print("The sequence {} is unique.".format(list_numbers))
    else:
        print("The sequence {} is NOT unique.".format(list_numbers))


main()
