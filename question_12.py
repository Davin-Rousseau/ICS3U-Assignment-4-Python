#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to enter classes held and attended
# and tells them if they can write an exam or not


def main():
    # This function calculates if student can write exam

    # input
    number = input("Enter number of classes held: ")
    number2 = input("Enter number of classes attended: ")
    print("")

    # process
    try:
        classes_held = int(number)
        classes_attended = int(number2)

        percentage = (classes_attended / classes_held) * 100
        print("The percentage of attendance is: {}%".format(percentage))

        if (percentage >= 75.0):
            print("You may take the exam.")

        else:
            print("You may not take the exam.")

    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
