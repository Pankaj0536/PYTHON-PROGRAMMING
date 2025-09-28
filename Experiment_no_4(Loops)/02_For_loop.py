#  In this file we will learn how to use for loop statements in python

# Task1 : Print number 0 to 10
print("Printing 0 to 10 : ")
for i in range(0 , 11):
    print(i , end = " ")
print("")

# Task2 : Print even number 1 to 20 
print("Printing even number 1 to 20 : ")
for i in range(1 , 21):
    if i % 2 == 0 :
        print(i , end = " ")
print(" ")

# Task 3 : Print your name 10 times
name = input("Enter your name : ")
for i in range(1 , 11):
    print(name ,end = " ")

