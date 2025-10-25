# Ask user for their personal details
name = input("Enter your name : ")          # Get user's name
Dept = input("Enter your department : ")    # Get user's department
age = int(input("Enter your age :"))        # Get user's age (converted to integer)

# Open a file named 'file.txt' in write mode ('w')
# If the file doesn't exist, it will be created automatically
f = open("file.txt", "w")

# Write user details into the file using 'file' parameter of print()
print(f"Name : {name} ", file=f)            # Write name to file
print(f"Department : {Dept} ", file=f)      # Write department to file
print(f"Age : {age} ", file=f)              # Write age to file

# Notify the user that details have been saved successfully
print("Student details printed in file 'file.txt' ")

# Close the file to free system resources and ensure all data is written properly
f.close()
