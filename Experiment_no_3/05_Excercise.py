# Excercise to Evaluate grade for given marks
# A: 90+, B: 75-89, C: 60–74, D: 40–59, F: below 40 (if-elif-else)

marks = int(input("Enter your marks : "))

if marks >= 90 and marks <= 100 :
    print(f"Marks : {marks} | Grade : A ")

elif marks >= 75 and marks <= 89 :
    print(f"Marks : {marks} | Grade : B ")

elif marks >= 60 and marks <= 74 :
    print(f"Marks : {marks} | Grade : C ")

elif marks >= 40 and marks <= 59 :
    print(f"Marks : {marks} | Grade : D ")

elif marks < 40 :
    print(f"Marks : {marks} | Grade : F ")
    
else:
    print("Invalid Marks.")
    