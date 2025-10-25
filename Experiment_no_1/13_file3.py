#  in this program we will combine the concept of file as well as flush 

import time
print("This is going to print at console ",flush = True)

with open("live_log.txt" ,"w") as f:
    for i in range(1 , 10):
        print(f"{i + 1} packets recieved ",file = f , flush = True )
        time.sleep(0.5)
f.close()