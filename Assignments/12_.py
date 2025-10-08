# Using lambda and map(), convert a list of temperatures in Celsius to Fahrenheit.
# Formula: F = C * 9/5 + 32.

# List of Temperature in celsius :
temp_celsius = [0 , 12 , 40 , 80 , 76 , 23]

to_fehrenheit = lambda c :  c * 9/5 + 32

# List of Temperature in Fehrenheit :
fehrenheit = list(map(to_fehrenheit , temp_celsius)) 
print("Temperature in Celsius : ",temp_celsius)

print("\nTemperature in fehrenheit : ",fehrenheit)