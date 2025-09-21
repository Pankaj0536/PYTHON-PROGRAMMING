# In this file we will learn how the typecasting work in python

num1 = 23       # Integer
num2 = 45.99    # float
num3 = 2 + 3j   # complex

a = float(num1)
b = int(num2)
c = str(num3)

print('Before typecasting')
print(num1,"     -> " , type(num1))
print(num2,"  -> " , type(num2))
print(num3," -> " , type(num3))

print('\n After typecasting')
print(a,"    -> " , type(a))
print(b,"      -> " , type(b))
print(c,"  -> " , type(c))