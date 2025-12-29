# In this excercise we will see some use case of dictionaries and solve many problems 

# 1) count the occurenceof number present in list '[1 , 1 , 8 , 9 , 3 , 4 ,3 , 4 , 8 , 8 ]'
list = [1 , 1 , 8 , 9 , 3 , 4 ,3 , 4 , 8 , 8]
print(f"list : {list}")

count = {}  # I am using dictionary whcih will store the count of each number
for l in list :
    if l in count :
       count[l] += 1  
    else :
        count[l] = 1

# Printing the final output : 
print("Frequency : ")
for num , freq in count.items() :
    print(num ,":", freq)

'''
Output :

list : [1, 1, 8, 9, 3, 4, 3, 4, 8, 8]
Frequency : 
1 : 2
8 : 3
9 : 1
3 : 2
4 : 2

'''