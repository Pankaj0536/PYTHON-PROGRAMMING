# In this file we have some basic functions defination and calling  

# function definations : 
def greet(name):    # With argument and without return value
    print(f"Hello! {name}")

def display() :     # Without arguments and without return value
    print("What a Beautiful Morning today")

def findings() :    # Without argument with return value
    return 21

def value(value) :  # With argument with return value
    return value * 3

# Function callings 

greet('Pankaj')
display()

print("Your findings is ",findings())

new_value = value(3)
print(f"New value is {new_value}")