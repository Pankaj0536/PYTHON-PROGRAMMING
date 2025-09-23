# In this file we will learn how tupes are used

Students = ("Pankaj" , "Rahul" , "Rohit" ,"Vinay" , "Nisha")

print("Students are : " , Students)

# immutable or  unchangable:

# Students[2] = "Chandan" 
# print("Students are : " , Students) 
# TypeError: 'tuple' object does not support item assignment

# We cant add new element in exixting tuple using append() function
# Students.append("john") not possible

#Whereas we can add new items using this approach
Students = Students + ("John",)
print(Students)

# output:
# Students are :  ('Pankaj', 'Rahul', 'Rohit', 'Vinay', 'Nisha')
# ('Pankaj', 'Rahul', 'Rohit', 'Vinay', 'Nisha', 'John')