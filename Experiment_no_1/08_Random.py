#In this file we we learn how an random number is generated in python 
import random
import time # Time module 

for i in range(100) :
    print(random.randrange(1, 70) , end = "," , flush = True)
    time.sleep(0.1)  # Not reuired 

'''
Output : 
33,67,41,53,4,25,63,63,40,18,69,67,57,32,69,47,40,31,50,36,50,38,27,11,38,51,12,45,61,69,16,68,43,3,42,20,51,37,38,23,35,6,20,39,67,22,34,9,66,44,61,21,14,46,59,65,43,60,35,10,64,51,7,26,40,59,58,6,26,11,44,65,27,37,16,66,56,43,52,11,28,23,19,43,53,45,55,39,64,34,17,69,23,38,43,31,35,2,22,9,
'''