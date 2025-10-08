# Create a function that accepts a variable number of arguments (*args) and returns their sum.

# Addition function which return sum of all argument passed 
def add_args(*args) :
    return sum(args)

# Variable number of parameters are pass to function
print(add_args(11 , 12 , 15 , 88 , 90 ))
print(add_args(23 , 67 , 8 ,44))
print(add_args(12 , 45))

'''
 Output :
 216
 142
 57
'''