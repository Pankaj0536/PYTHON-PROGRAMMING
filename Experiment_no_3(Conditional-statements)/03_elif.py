#  Hey guys in this file we will explore an example of elif statements in python


# user input
num  = int(input("Enter the value of num : "))

if (num > 0 ) :
    print(f"Number {num} is positive.")

elif (num < 0 ):
    print(f"Number {num} is negative.")

else :
    print(f"Number {num} is zero ")

""" Output :

Enter the value of num : 56
Number 56 is positive.

Enter the value of num : -89
Number -89 is negative.

Enter the value of num : 0
Number 0 is zero 
 """