# In this file we will learn how we can use recursion for factorial count

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n-1)

num = int(input("Enter any number for factorial count : "))

print(f"{num}! = {factorial(num)}")