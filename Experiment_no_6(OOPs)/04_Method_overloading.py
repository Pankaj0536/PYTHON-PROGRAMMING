#  In this code we will learn method overloading in python

class Society:

    def greet(self, name=None, surname=None):
        if name is not None and surname is not None:
            print(f"Good morning {name} {surname}")
        elif name is not None:
            print(f"Hello {name}")
        else:
            print("Hello there!")

# create object
society_obj = Society()

society_obj.greet("Pankaj")            # calls one-argument version
society_obj.greet("Pankaj", "Rana")  # calls two-argument version
society_obj.greet()                    # calls no-argument version

'''
output :

Hello Pankaj
Good morning Pankaj Rana
Hello there!

'''