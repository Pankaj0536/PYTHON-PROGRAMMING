# In this file we will learn to use the break statements

while 1 :
    num = int(input("Enter any value (Enter 0 to stop) : "))

    if num == 0:
        print("Stopping the Execution....")
        break
    if num % 2 == 0 :
        print(f"Number {num} is even")
    else :
        print(f"Number {num} is odd")

'''
Output : 
Enter any value (Enter 0 to stop) : 2
Number 2 is even
Enter any value (Enter 0 to stop) : 1
Number 1 is odd
Enter any value (Enter 0 to stop) : 0
Stopping the Execution....
'''