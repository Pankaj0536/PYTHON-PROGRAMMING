# Write Python code to display the multiplication table of 5 using a for loop.

num = int(input("Enter any number : "))

for i in range(1 , 11) :
    print(f"{num} * {i} = {num * i}")

'''
output :
Enter any number : 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''