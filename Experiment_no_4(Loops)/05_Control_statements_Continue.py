# program to use the continue statements in python

i,num = 0 , int(input("Enter any value : "))

while i <= num :
    i = i + 1
    if i % 2 == 0 :
        continue
    print(i, end = " ")