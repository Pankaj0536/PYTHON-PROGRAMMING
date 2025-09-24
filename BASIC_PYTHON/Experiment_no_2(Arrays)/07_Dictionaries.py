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

# output : 
# Original Dictionary :  {'name': 'pankaj Rana', 'Roll Number': 23, 'Div': 'B'}
# Modified roll numbers  {'name': 'pankaj Rana', 'Roll Number': 78, 'Div': 'B'}
# Added age :   {'name': 'pankaj Rana', 'Roll Number': 78, 'Div': 'B', 'Age': 19}
# Deleted Div :  {'name': 'pankaj Rana', 'Roll Number': 78, 'Age': 19}