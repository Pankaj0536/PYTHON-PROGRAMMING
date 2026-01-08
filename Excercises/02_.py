'''
Aim : 
The Title Case Fixer Given a string, capitalize the first letter of every word except for a list of small words (like "and", "the", "of", "in"). However, the first word of the string must always be capitalized.

Focus: .split(), .capitalize(), and list membership.
'''

text = input("Enter the string : ").lower()

splited_list = text.split()

Exception = ["and", "the", "of", "is" ,"in"]

for i in range(len(splited_list)):
    if i == 0 :
        splited_list[i] = splited_list[i].capitalize() 

    elif (splited_list[i- 1].endswith(".")):
        splited_list[i] = splited_list[i].capitalize() 
    elif splited_list[i] not in Exception :
        splited_list[i] = splited_list[i].capitalize() 
    else :
        splited_list[i] = splited_list[i].lower()

print("\nCapitalized string : ")
print(" ".join(splited_list))

'''
Output :
 Enter the string : Gravitational acceleration (symbolized as g) is the acceleration an object experiences due to gravity, measured in meters per second squared (m/s²).

Capitalized string :
Gravitational Acceleration (symbolized As G) is the Acceleration An Object Experiences Due To Gravity, Measured in Meters Per Second Squared (m/s²).

'''

