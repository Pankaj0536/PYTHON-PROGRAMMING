# In this file we will learn how file are used

print("---List---")

Vegetables = ["Carrot" , "Potato" , "Cucumber" , "Onion"]

print(" Vegetables   : ",Vegetables)


# mutable or changeble
Vegetables[-1] = "cabbage"
print("Vegetables are : ",Vegetables)

# Adding Vegetable in exesting list
Vegetables.append("Chilly") # append() function is used to add anyhthing in existing collection
Vegetables.insert(2 ,"tomato") #To insert at any position
print("Vegetables list ", Vegetables)

# Remove any element
Vegetables.remove("Carrot")
print("Onion is removed",Vegetables)
print('This is by poping function',Vegetables.pop())

# Duplicate allowed
stationary = ['Pen','Pencil' , 'Eraser' ,'Pen']
print("My Stationary are :" ,stationary)

# output:
# ---List---
#  Vegetables   :  ['Carrot', 'Potato', 'Cucumber', 'Onion']
# Vegetables are :  ['Carrot', 'Potato', 'Cucumber', 'cabbage']
# Vegetables list  ['Carrot', 'Potato', 'Cucumber', 'cabbage', 'Chilly']
# My Stationary are : ['Pen', 'Pencil', 'Eraser', 'Pen']
