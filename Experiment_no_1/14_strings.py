# In this file we will deeply understand the cocept of strings python

# string : Anything enclosed in quotes is string 
# example :
name = "Maharastra"
print("String is  : ",name)
print(f"The length of string {name} is {len(name)}")


# Slicing of string ``string[start:end:step]``start(included) , end(excluded)
# example : 

# Basic slicing :
print("\nBasic slicing :")
print("name[0:6] : ",name[0: 6]) # Print from M to r
# Omitting start or end :
print("\nOmitting start or end : ")
print("name[:5]",name[:5]) # start omitted
print("name[4:]",name[4:]) # end omitted

# Using step
print("\nUsing step:")
print("name[::2]",name[::2]) # step size will be 2 
print("name[::-7]",name[::-7]) # len - 7 : 10 - 7 = 3 (Step size will be 3)
print("Reversed string or name[::-1]",name[::-1]) # the string will reversed cause len - 1 : 10 - 1 = 9 (this wiil be step size)

# Using negative index 
print("\nUsing negatie index:")
print("name[-3 : -5 : -1]",name[-3: -5 :-1]) # len - 3 to len -6
print("name[-5 : -2]",name[-5:-2]) # len -5 to len -2 will be print 

'''
Output :
String is  :  Maharastra
The length of string Maharastra is 10

Basic slicing :
name[0:6] :  Mahara

Omitting start or end :
name[:5] Mahar
name[4:] rastra

Using step:
name[::2] Mhrsr
name[::-7] ah
Reversed string or name[::-1] artsarahaM

Using negatie index:
name[-3 : -5 : -1] ts
name[-5 : -2] ast
'''