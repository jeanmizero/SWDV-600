# Declare a function
def happy():
    print('Happy birthday to you!')
# happy()


def sing(person):
    happy()
    happy()
    print('Happy birthday, dear ', person + '.')
    happy()

# sing('Joe')


def main():
    sing('Fred')
    print()
    sing('Lucy')
    print()
    sing('Smith')


main()
