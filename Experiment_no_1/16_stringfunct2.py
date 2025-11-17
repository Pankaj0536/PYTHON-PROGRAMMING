# In this file we will complete rest of our python string fuction


# 11. 'find()' Method 
# this method returns index number of first occuring value else -1(If absent)
# eg : 
intro = "Hey this is pankaj here! "
print("Value 'is' is present at index :" ,intro.find("is"))
# if absent -- returns -1 
print("index number : ",intro.find("Lion"))

# 12. 'index()' Method (similar to find() method)
_str = "Hey this is a string"
print("String :",_str)
print("the value 'ing' is at : ",_str.index("ing"))
# If absent 
# print("Index is ",_str.index("why"))

# 13. 'isalnum()' Method
isalnum_string = "Heythississpankajhere123"
print("Result1 :",isalnum_string.isalnum()) #true
isalnum_string2 = "white spaces are there!"
print("Result2 :",isalnum_string2.isalnum())

# 14. 'isalpha()' Method
print("\n isalpha() method analysis")
isalpha_str1 = "Thisisstring"
isalpha_str2 = "123pankaj"
print("Result1 : ",isalpha_str1.isalpha())
print("Result2 : ",isalpha_str2.isalpha())

# 15. 'islower' method 
checkstr = "Hey this is string"
print(checkstr.islower()) # false

checkstr2 = "wohhhh!"
print(checkstr2.islower()) #true

# 16. 'isprintable' Method
print("\n isprintable() check : ")
temp = "all string are printable"
print(temp.isprintable())   #true
temp2 = "all string are \n printable"
print(temp2.isprintable())  #false

# 17. isspace() Method
spaced_string = "    wohhh!!!"
print(" Isspace check:\n",spaced_string.isspace())  # false
spaced_string2 = "      "
print("",spaced_string2.isspace())  #true
 
# 18. istitle() Method
title_check = "Save Water Save Life"
print(title_check.istitle())    #true
title_check2 = "what's happend"
print(title_check2.istitle())   #false

# 19. isupper() Method
string_upper = "HELLO PANKAJ HERE!"
print(string_upper.isupper())   #true

# 20.startwith() Method
tempstr = "Hey this is string"
print("Result : ",tempstr.startswith("Hey")) # true
print("Result : ",tempstr.startswith("is")) # false

# 21.swapcase() Method
string_converter = "Doraemon IS my favoritE cartoon!"
print(string_converter.swapcase())

