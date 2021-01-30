# Make library available
import math


def main():
    print("Quadratics function")
    print()

    a = float(input("Enter coefficient a : "))
    b = float(input("Enter coefficient b : "))
    c = float(input("Enter coefficient c : "))

    disc_root = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + disc_root) / (2 * a)
    root2 = (+b + disc_root) / (2 * a)
    print()
    print("Solution are:", root1, root2)


main()
