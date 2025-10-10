# Write a Python program that raises a user-defined exception if the entered age is less than 18.

# Define a user-defined exception
class AgeTooSmallError(Exception):
    pass

# Take input from user
age = int(input("Enter your age: "))

# Check age and raise exception if less than 18
try:
    if age < 18:
        raise AgeTooSmallError("Age is less than 18! Access denied.")
    else:
        print("Access granted.")
except AgeTooSmallError as e:
    print(f"Error: {e}")

'''
Output
Enter your age: 34
Access granted.
'''
