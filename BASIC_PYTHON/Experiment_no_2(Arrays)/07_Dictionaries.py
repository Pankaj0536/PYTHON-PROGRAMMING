# In this file we will learn to use dictionaries

students = {
    "name" : "pankaj Rana",
    "Roll Number" : 23,
    "Div" : 'B'
}

print("Original Dictionary : " ,students)

#modifying roll number to 78
students["Roll Number"] = 78
print("Modified roll numbers ",students)

# Adding new element
students["Age"] = 19
print("Added age :  ",students)

#deleting div
del students["Div"]
print("Deleted Div : ",students)

# Keys and Values in dictionary 
print("Keys:", list(students.keys()))
print("Values:", list(students.values()))


print("\nFinal dictionary:")
for key, value in students.items():
    print(f"{key} => {value}")



# output : 
#Original Dictionary :  {'name': 'pankaj Rana', 'Roll Number': 23, 'Div': 'B'}
# Modified roll numbers  {'name': 'pankaj Rana', 'Roll Number': 78, 'Div': 'B'}
# Added age :   {'name': 'pankaj Rana', 'Roll Number': 78, 'Div': 'B', 'Age': 19}
# Deleted Div :  {'name': 'pankaj Rana', 'Roll Number': 78, 'Age': 19}
# Keys: ['name', 'Roll Number', 'Age']
# Values: ['pankaj Rana', 78, 19]

# Final dictionary:
# name => pankaj Rana
# Roll Number => 78
# Age => 19