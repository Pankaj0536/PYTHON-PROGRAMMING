# This is my one of the beautiful console based project 

# greeting string (centered in console using '*' as padding)
greet = "Welcome to String Analyser"
print(greet.center(100, "*"))

# Asking user to enter any string for processing
input_string = input("Enter your string : ")

# Showing available operations to the user
print("\n____________________________OPERATIONS______________________________________")
print("Enter 1 - > To Uppercase\n"
      "Enter 2 - > To Lowercase\n"
      "Enter 3 - > To Strip(remove white spaces from start/end)\n"
      "Enter 4 - > To rstrip(remove any trailing character)\n"
      "Enter 5 - > To replace(replace any value from another)\n"
      "Enter 6 - > To split(split the string into list)\n"
      "Enter 7 - > To capatalize(convert first character to uppercasee and rest lower)\n"
      "Enter 8 - > To count(count the occurence of any value)\n"
      "Enter 9 - > To endswith check (check if your string is ending with particular value or not)\n"
     )

# Taking user operation choice
ch = int(input("Your choice : "))
print("__________________________________________________________________\n")

# Using match-case for operation selection (Python 3.10+ feature)
match ch:
    case 1:
        # Convert string to UPPERCASE
        print(f"String : {input_string}")
        print(f"In uppercase : {input_string.upper()}")

    case 2:
        # Convert string to lowercase
        print(f"String : {input_string}")
        print(f"In Lowercase : {input_string.lower()}")

    case 3:
        # Remove white spaces at beginning and end
        print(f"String : {input_string}")
        print(f"Striped string : {input_string.strip()}")

    case 4:
        # Remove a specific trailing character (user input)
        x = input("Enter character to be removed :")
        print(f"String : {input_string}")
        print(f"Final string: {input_string.rstrip(x)}")

    case 5:
        # Replace occurrences of a substring with another substring
        print("format :\n\t x : will replaced\n\t y : going to replace x")
        print(f"Your string : {input_string}")
        x, y = input("Enter x :"), input("Enter y :")
        print(f"Before: {input_string}")
        print(f"After : {input_string.replace(x, y)}")

    case 6:
        # Split the string using given separator into a list
        x = input("Enter spacing character : ")
        print(f"String : {input_string}")
        print(f"splitted string : {input_string.split(x)}")

    case 7:
        # Make first character uppercase and rest lowercase
        print(f"String : {input_string}")
        print(f"Final string : {input_string.capitalize()}")

    case 8:
        # Count the occurrence of a value/character in string
        val = input("Enter value to be count : ")
        print(f"String : {input_string}")
        print(f"'{val}' Count : {input_string.count(val)}")

    case 9:
        # Check if string ends with given value
        endswithch = input("Enter ends with value : ")
        print(f"String : {input_string}")
        print(f"is ends with '{endswithch}' : {input_string.endswith(endswithch)}")

    case _:
        # Invalid input handling
        print("ERROR::INVALID CHOICE!!")

print("__________________________________________________________________")
