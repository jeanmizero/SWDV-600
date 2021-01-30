# Exercise 2
def total_score():
    number_of_days = int(input("How many days of scores? "))

    total_score = 0
    for day in range(1, number_of_days+1):
        score_for_day = int(input("Enter score for day" + str(day) + ": "))
        total_score += score_for_day

    print("The total score of the", number_of_days, "days is", total_score)


total_score()
