# Exercise 1
# Make library available
import math


def filler():
    number_of_bowling_ball = int(
        input("How many bowling balls will be manufactured? "))
    ball_diameter_in_inch = float(
        input("What is the diameter of each ball in inches? "))
    core_volume = float(input("What is the core volume in inches cubed? "))

    # sphere volume = (4/3)pi * r ** 3
    diameter_in_inch = 8.5
    radius = float(diameter_in_inch / 2)
    sphere_volume = (4/3) * math.pi * pow(radius, 3)
    # print(sphere_volume)
    total_filler = (sphere_volume - core_volume) * number_of_bowling_ball
    print("You will need ", total_filler, "inches cubed of filler")


filler()
