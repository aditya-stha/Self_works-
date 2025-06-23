array=[[ 0 for col in range(10)] for row in range(10) ]
import random
# inward loop indicating columns first and the outward loop for rows 
for row in range (10):
    for col in range(10):
        array[row][col]= random.randint(0,100)
        print ( array[row][col], end =" ")
    print()



for row in range(10):
    upperbound=10
    while upperbound>0:
        swaps=False
        for col in range(upperbound-1):
            if array[row][col] > array[row][col+1]:
                swaps=True
                temp=array[row][col+1]
                array[row][col+1]=array[row][col]
                array[row][col]=temp
        if swaps==False:
            break
        else:
            upperbound-=1
    
            
for row in range (10):
    for col in range(10):
        print ( "|"+str(array[row][col])+"|", end =" ")
    print()
           
    
    
