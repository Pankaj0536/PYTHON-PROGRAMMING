# In this file we will learn to use switch statement in python

# This include the program to find the weekday using number(1 to 7)

day = int(input("Enter day number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
