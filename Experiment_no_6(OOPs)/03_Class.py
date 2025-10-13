# Program to avail bonus with respect to position :

class employee:

    def __init__(self , name , department , position , salary):
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary

    def bonus(self , percent) :
        bonus = (percent * self.salary)/100
        return bonus


    def final_salary(self) :
        if self.position.upper() == "MANAGER":
            self.salary += self.bonus(20)
            return self.salary
        
        if self.position.upper() == "HR":
            self.salary += self.bonus(10)
            return self.salary
        
        if self.position.upper() == "DEVELOPER":
            self.salary += self.bonus(5)
            return self.salary
            
    def display(self):
        print("\nEmployee Information :")
        print(f"Name = {self.name}")
        print(f"Department = {self.department}")
        print(f"Position = {self.position}")
        print(f"salary = {self.salary}")
        print("salary with bonus =",self.final_salary())
 
name = input("Enter your name : ")
department = input("Enter your department : ")
position = input("Enter Your position : ")
salary = float(input("Enter Your salary : "))

obj = employee(name , department , position , salary)
obj.display()

'''
 Output :
Employee Information :
Name = Pankaj Rana
Department = Technical
Position = Manager
salary = 120000.0
salary with bonus = 144000.0
'''