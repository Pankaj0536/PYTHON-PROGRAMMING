# Basic calculator project using operators 
import time 

# starting calculator with loading bar
print("Opening calculator: " , end = "" , flush = True)
for i in range(1 , 100 ):
    print("█",end = "" , flush = True)
    time.sleep(0.001)
print(" GO!")

# defining functions for operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x , y):
    return x*y

def division(x , y):
    try :
        return x / y
    except ZeroDivisionError:
        print("Error::Cannot divide by 0")
    

def power(x , y):
    return x ** y

# main function

print("-----------------------------------------------------Calculator-------------------------------------------------------")


while 1 :
    print("Enter 1 -> Addtion\nEnter 2 -> Subraction\nEnter 3 -> Multiplication\nEnter 4 -> Division\nEnter 5 -> Power\nEnter 6-> Exit")
    ch = int(input("Enter your choice : "))
    match ch :
        case 1:
            print("-----------------------------------------------------Addition-------------------------------------------------------")
            x , y = int(input("Enter x : ")), int(input("Enter y : "))
            print(f"\n x = {x}\n y = {y}")
            print(f" {x} + {y} = {add(x ,y)}")

        case 2 : 
            print("-----------------------------------------------------Subtraction-------------------------------------------------------")
            x , y = int(input("Enter x : ")), int(input("Enter y : "))
            print(f"\n x = {x}\n y = {y}")
            print(f" {x} - {y} = {subtract(x ,y)}")

        case 3 :
            print("-----------------------------------------------------Multiplication-------------------------------------------------------")
            x , y = int(input("Enter x : ")), int(input("Enter y : "))
            print(f"\n x = {x}\n y = {y}")
            print(f" {x} X {y} = {multiply(x ,y)}")

        case 4 :
            print("-----------------------------------------------------Division-------------------------------------------------------")
        
            nemo , deno = int(input("Enter neumerator : ")), int(input("Enter denominator : "))
            print(f"\n nemo = {nemo}\n deno = {deno}")
            print(f" {nemo} / {deno} = {division(nemo,deno)}\n")
            

        case 5 :
            print("-----------------------------------------------------Power-------------------------------------------------------")
            x , y = int(input("Enter x : ")), int(input("Enter y : "))
            print(f"\n x = {x}\n y = {y}")
            print(f" {x} ^ {y} = {power(x ,y)}")

        case 6 :
            print("Closing calculator: " , end = "" , flush = True)
            for i in range(1 , 100 ):
                print("█",end = "" , flush = True)
                time.sleep(0.001)
            print(" Bye!")            
            break

        case _ :
            print("Invalid choice!!")

'''
Output :
Opening calculator: ███████████████████████████████████████████████████████████████████████████████████████████████████ GO!
-----------------------------------------------------Calculator-------------------------------------------------------
Enter 1 -> Addtion
Enter 2 -> Subraction
Enter 3 -> Multiplication
Enter 4 -> Division
Enter 5 -> Power
Enter 6-> Exit
Enter your choice : 1
-----------------------------------------------------Addition-------------------------------------------------------
Enter x : 23
Enter y : 56

 x = 23
 y = 56
 23 + 56 = 79
Enter 1 -> Addtion
Enter 2 -> Subraction
Enter 3 -> Multiplication
Enter 4 -> Division
Enter 5 -> Power
Enter 6-> Exit
Enter your choice : 4
-----------------------------------------------------Division-------------------------------------------------------
Enter neumerator : 45
Enter denominator : 0

 nemo = 45
 deno = 0
Error::Cannot divide by 0
 45 / 0 = None

Enter 1 -> Addtion
Enter 2 -> Subraction
Enter 3 -> Multiplication
Enter 4 -> Division
Enter 5 -> Power
Enter 6-> Exit
Enter your choice : 9
Invalid choice!!
Enter 1 -> Addtion
Enter 2 -> Subraction
Enter 3 -> Multiplication
Enter 4 -> Division
Enter 5 -> Power
Enter 6-> Exit
Enter your choice : 5
-----------------------------------------------------Power-------------------------------------------------------
Enter x : 3
Enter y : 4

 x = 3
 y = 4
 3 ^ 4 = 81
Enter 1 -> Addtion
Enter 2 -> Subraction
Enter 3 -> Multiplication
Enter 4 -> Division
Enter 5 -> Power
Enter 6-> Exit
Enter your choice : 6
Closing calculator: ███████████████████████████████████████████████████████████████████████████████████████████████████ Bye!
'''