# Write a Python program that takes a number from the user and prints whether it is even or odd.

while 1 :
    value = input("Enter the value(Enter 's' to stop): ")

    # Case conversion if user enter 'S' instead of 's'
    if value.lower() == 's':
        print("Exiting the loop..")
        break
    
    value = int(value)
    if value % 2 == 0 :
        print(f"Number {value} is even ")  
              
    else :
        print(f"Number {value} is odd ")    
    
# Output :
# Enter the value(Enter 's' to stop): 23
# Number 23 is odd 
# Enter the value(Enter 's' to stop): 12
# Number 12 is even 
# Enter the value(Enter 's' to stop): S
# Exiting the loop..