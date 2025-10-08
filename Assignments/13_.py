# Create a class Car with attributes brand and year
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print(f"Car brand: {self.brand} of year: {self.year}")

# Create an object of the class
obj = Car("Rolls Royce", 2012)

# Display the attributes
obj.display()

'''
Output : Car brand: Rolls Royce of year: 2012
'''