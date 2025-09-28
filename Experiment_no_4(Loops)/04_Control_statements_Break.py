# In this file we will learn to use the break statements

while 1 :
    num = int(input("Enter any value (Enter 0 to stop) : "))
    if num % 2 == 0 :
        print(f"Number {num} is even")
    else :
        print(f"Number {num} is odd")
    if num == 0:
        break