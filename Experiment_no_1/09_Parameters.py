'''
 In this file we will learns and use some parameters  in print statements
 print(object(s), sep, end, file, flush)
    sep: It is an optional parameter used to define the separation among different objects to be printed.
    end is also a pramentr , definethat how the print statement going to end 
 '''

# example :

# Use of sep parameter 
name = "pankaj"
age = 19

print(name , age , 23, sep = ' -> ')

# use of end parameter
print ("Hey this is pankaj here", end = " ")
print("and pankaj age is 19")

#  there are many parameters in python like file , flush

'''
Output :

pankaj -> 19 -> 23
Hey this is pankaj here and pankaj age is 19

'''