# In this file we will learn to use if elif else statements 

from datetime import datetime # this is for current time

name = input("Enter your name : ")
current = datetime.now()
hour_value = current.hour

if hour_value >= 12 and hour_value < 16:
    print(f"Good Afternooon {name}")

elif hour_value >= 1 and hour_value < 12:
    print(f"Good Morning {name}")

elif hour_value >= 16 and hour_value < 20:
    print(f"Good Evening {name}")

else :
    print(f"Good Night {name}")
    