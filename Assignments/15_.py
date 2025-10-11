# Write a Python program to handle ZeroDivisionError when dividing two numbers
# entered by the user.

try :
    n = int(input("Enter Numerator :"))
    d = int(input("Enter Denominator : "))
    print(f"The value of {n} / {d} = {n/d}")
except ZeroDivisionError :
    print("Error :: Cannot divide by Zero")

'''
output :

Enter Numerator :45
Enter Denominator : 4
The value of 45 / 4 = 11.25

Enter Numerator :34
Enter Denominator : 0
Error :: Cannot divide by Zero

'''