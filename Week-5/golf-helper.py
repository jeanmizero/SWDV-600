def main():
    print("Welcome to the Golf Club Helper!")
    print("Tell me your situation, and I'll recommend a club \n")

    green_ball = input("Did you hit it on the green (y/n)? ")
    distance = int(input("How far is the ball from the hole? "))
    print()

    if green_ball == "y":
        print("I recommend using your Putter")
    else:
        if distance >= 200:
            print("I recommend using your Driver")
        elif distance >= 140:
            print("I recommend using your 5-Iron")
        elif distance >= 100:
            print("I recommend using your 9-Iron")
        else:
            print("I recommend the Pitching Wedge")


main()
