# In this file we will see the various string functions in pyhton

# 1. upper() : name suggest to convert a string in uppercase
name = "Pankaj Rana"
print(f"Your name is : {name.upper()}")

# 2. lower() : similar to upper but this convert to lowercase
status = "SleepIng"
print(f"Your status is : {status.lower()}")


# 3. strip() : This remove white spaces from string befor or after written
friend = " Hafiz khan "
print(f"Your friend name is {friend.strip()}")

# 4. rstrip() : it removes any trailing character from end in string 
str = "yeeepeee!!!@@"
print(f"removed '@' from {str} : ",str.rstrip("@"))

# 5. replace : name suggest this is use to replace specific occurence of a string with another string  
replaced_name = name.replace('a' , '@')
print("name is : ", replaced_name)

# 6. split() : it split a string to a list with a given value 
print("The list of you name is : ",name.split(" "))

# 7. capitalize() : it cover the first character of a string in uppercase and rest of lowercase
str2 = "heY this is PANKAJ here!!"
print(str2.capitalize())

# 8. center() : it is use to print in center of console 
str3 = "WElcome to my code"
print((str3.capitalize()).center(50 , "*"))

# 9. count() : it is use to count the occurence of any number or value in a given string 
print(f"In string {name} there is {name.count("a")} time of 'a'")

# 10. endswith : this is use to check wheter the given string is ending with the given value(if yes then return true else false )
print(f"Is string '{name}' is ending with 'na' : {name.endswith("na")}")

#  we can check whether my given value is lying in between my given range 
print(f"Is the 'kh' is lying in between 6 - 9 in string {friend} : {friend.endswith("kh" , 6 , 9)}")

'''
Output window :

Your name is : PANKAJ RANA
Your status is : sleeping
Your friend name is Hafiz khan
removed '@' from yeeepeee!!!@@ :  yeeepeee!!!
name is :  P@nk@j R@n@
The list of you name is :  ['Pankaj', 'Rana']
Hey this is pankaj here!!
****************Welcome to my code****************
In string Pankaj Rana there is 4 time of 'a'
Is string 'Pankaj Rana' is ending with 'na' : True
Is the 'kh' is lying in between 6 - 9 in string  Hafiz khan  : True

'''