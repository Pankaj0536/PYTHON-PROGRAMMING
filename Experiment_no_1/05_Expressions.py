# This file contain various expressions in python
# Example : a + b / 8 - c * 3 + a**b
a , b = 2 , 4 # declaration can be done in this way if more variable is initialize at same time
c , d = 6 , 12

z = a + b / 8 - c * 3 + a**b # expression

# one Way to print the value of variables 
print(' a = {a}\n b = {b}\n c = {c}\n d = {d}'.format(a=a,b=b,c=c,d=d))

print(' a + b / 8 - c * 3 + a**b = ',z)

# output :
 # a = 2
 # b = 4
 # c = 6
 # d = 12
 # a + b / 8 - c * 3 + a**b =  0.5
