# In this file we will learn how file are used

print("---List---")

Vegetables = ["Carrot" , "Potato" , "Cucumber" , "Onion"]

print(" Vegetables   : ",Vegetables)


# mutable or changeble
Vegetables[-1] = "cabbage"
print("Vegetables are : ",Vegetables)

# Adding Vegetable in exesting list
Vegetables.append("Chilly") # append() function is used to add anyhthing in existing collection
print("Vegetables list ", Vegetables)

# Duplicate allowed

stationary = ['Pen','Pencil' , 'Eraser' ,'Pen']
print("My Stationary are :" ,stationary)

# output:
# ---List---
#  Vegetables   :  ['Carrot', 'Potato', 'Cucumber', 'Onion']
# Vegetables are :  ['Carrot', 'Potato', 'Cucumber', 'cabbage']
# Vegetables list  ['Carrot', 'Potato', 'Cucumber', 'cabbage', 'Chilly']
# My Stationary are : ['Pen', 'Pencil', 'Eraser', 'Pen']
