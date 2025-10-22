# Create a list of dictionaries to represent multiple students.

student1 = { 
    "name" : "Pankaj",
    "age" : 19,
    "roll no" : 23
}

student2 = { 
    "name" : "Hafiz",
    "age" : 19,
    "roll no" : 19
}

student3 = { 
    "name" : "Nikhil",
    "age" : 20,
    "roll no" : 9
}

# List of students
list_of_student = [student1 , student2 , student3]

print("Student1 Details")
for key , value in student1.items():
    print(f"{key} => {value}")

print("\nStudent2 Details")
for key , value in student2.items():
    print(f"{key} => {value}")

print("\nStudent3 Details")
for key , value in student3.items():
    print(f"{key} => {value}")

print("\nlist of dictionaries to represent multiple students : ")
print(list_of_student)

'''
 output:
 Student1 Details
 name => Pankaj
 age => 19
 roll no => 23
 Student2 Details
 name => Hafiz
 age => 19
 roll no => 19
 Student3 Details
 name => Nikhil
 age => 20
 roll no => 9
 list of dictionaries to represent multiple students :
 [{'name': 'Pankaj', 'age': 19, 'roll no': 23}, {'name': 'Hafiz', 'age': 19, 'roll no': 19}, {'name': 'Nikhil', 'age': 20, 'roll no': 9}]
 '''