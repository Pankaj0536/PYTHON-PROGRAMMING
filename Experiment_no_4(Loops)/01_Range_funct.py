# Hey buddys in this file we will deeply understand the working of range() function

# Basically range() function is use with loops (especially with for loop) , by using range() we can print value from certain start to end
# range(stop) - it define tilll where you want to print
for i in range(5):
    print(i ,end = " ") # 0 1 2 3 4(last value in not included)

print()
# range(start, stop) - it define from where to where you want to print number 
for p in range(2 , 7):
    print(p, end = " ") # 2 3 4 5 6 

print()
# range(start , stop , step) - basically step is use to define increment/decrement (by default it is 1 when you not write any thing there)
for j in range(1 , 9 , 2 ):
    print(j, end = " ") # 1 3 5 7 (here 2 become the step size)

print()
# for decrement we should write negative value in step place
for k in range(10 , 0 , -2 ):
    print(k , end = " ") # 10 8 6 4 2 
