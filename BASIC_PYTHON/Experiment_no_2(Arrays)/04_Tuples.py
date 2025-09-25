# In this file we will learn how tupes are used

Students = ("Pankaj" , "Rahul" , "Rohit" ,"Vinay" , "Nisha") #tuple

print("Students are : " , Students)

# immutable or  unchangable check :

try:
    Students[2] = "Chandan" # This will raise an error
except TypeError as e:
    print("Tuples are immutable:", e)

# Adding element :

# We cant add new element in existing tuple using append() function
# Students.append("john") not possible

#Whereas we can add new items using this approach
Students = Students + ("John",)
print(Students)

# Dublicate are allowed in tuples :
Students = Students + ("Pankaj",)
print("New Tuples is ",Students)
print("Count of Pankaj is " ,Students.count("Pankaj"))

# output:
# Students are :  ('Pankaj', 'Rahul', 'Rohit', 'Vinay', 'Nisha')
# Tuples are immutable: 'tuple' object does not support item assignment
# ('Pankaj', 'Rahul', 'Rohit', 'Vinay', 'Nisha', 'John')
# New Tuples is  ('Pankaj', 'Rahul', 'Rohit', 'Vinay', 'Nisha', 'John', 'Pankaj')
# Count of Pankaj is  2