#In this file we we learn how an random number is generated in python 
import random

while True:
    try:
        num = int(input("How many random numbers (1-70) would you like to generate? "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"\nGenerating {num} random numbers between 1 and 70:")
for i in range(num):
    print(random.randint(1, 70))
