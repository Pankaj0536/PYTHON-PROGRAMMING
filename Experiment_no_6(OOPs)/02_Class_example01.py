#  In this file we will implement simple class example 

class car :

    def __init__(self , brand , year):
        self.brand =  brand 
        self.year = year 

    def display(self):
        print(f"Car Brand : {self.brand}\nYear : {self.year}")

# Object creation :
obj = car("Rolce Royce" , 2025)

# method calling
obj.display()


