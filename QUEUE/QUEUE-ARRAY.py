def initialize_queue():                   
    global startpointer,nextfreepointer,queuefull,queue,freeslots,queueempty,dtype,datatype,queuedefined
    length=int(input("Enter Queue Size:"))
    dtype=int(input("ENTER DATA TYPE [ 0 - INTEGER | 1 - STRING ]:"))
    match dtype:
                    case 0:
                        datatype=0
                    case 1:
                        datatype="" 
    queue=[datatype for index in range(length)]
    startpointer=0
    nextfreepointer=0
    queuefull=False
    queueempty=True
    queuedefined=True
    freeslots=len(queue)

def getcommand():
    global queuedefined
    while True:
        print("[ 0 - INITIALIZE QUEUE | 1 - Enqueue | 2 - Dequeue]")
        print("[ 3 - VEIW (UNORDER)   | 4 - VEIW    | 5 - SEARCH ]")
        print("[          6 - AUTOFILL      |        7 - END     ]")
        command=int(input("ENTER COMMAND:"))
        if command > -1 and command < 8:
              break
        else:
            print("INVALID COMMAND")
            
    if queuedefined == False:
            print("ERROR : QUEUE UNDEFINED -  AUTO DEFINING INITIATED")
            initialize_queue()
            
    return command

def Enqueue(data):
    global startpointer,nextfreepointer,queuefull,queue,freeslots,queueempty
    status=False
    if queuefull==False:
        queue[nextfreepointer]=data
        nextfreepointer+=1
        freeslots=freeslots-1
        if nextfreepointer==len(queue):
            nextfreepointer=0
        if freeslots==0:
            queuefull=True
        queueempty=False
        status=True
    return status

def Dequeue(datatype):
    global startpointer,nextfreepointer,queuefull,queue,freeslots,queueempty
    status=True
    data=datatype
    temp=datatype
    if queueempty==False:
        if queuefull==True:
            data=queue[startpointer]
            queue[startpointer]=temp
            nextfreepointer=startpointer
            startpointer+=1
            queuefull=False
            if startpointer==len(queue):
                startpointer=0
            freeslots=freeslots+1
            
        else:
            data=queue[startpointer]
            queue[startpointer]=temp
            startpointer+=1
            if startpointer==len(queue):
                startpointer=0
            freeslots=freeslots+1
            if freeslots==len(queue):
                queueempty=True   
    else:
        status=False
    return status,data
    
def veiw():
    global queue,startpointer,nextfreepointer,freeslots,queuefull,queueempty
    if queueempty==False:
        counter=startpointer
        for index in range(len(queue)-freeslots):
            print(f"[ {index+1} | {queue[counter]} ]")
            counter+=1
            if counter==len(queue):
                counter=0
    else:
        print(" QUEUE EMPTY UNABLE TO SHOW IN ORDER " )
        
        
        
    

def veiw_unordered():
    global queue,startpointer,nextfreepointer,freeslots,queuefull,queueempty
    for index in range(len(queue)):
        print(f"[ {index} | {queue[index]} ]")
    if queuefull==True:
        print(" QUEUE FULL ")
    elif queueempty==True:
        print("QUEUE EMPTY")
    else:
        print(f" START POINTER = {startpointer} |  FREE POINTER = {nextfreepointer} | FREE  SLOTS = {freeslots} ")

def random_string(MAX,MIN):
    import random
    choice=["num","symbol","chars","c_chars"]
    num="0123456789"
    length=random.randint(MIN,MAX)
    chars=" abcdefghijklmnopqrstwuvxyz"
    c_chars="ABCDEFGHIJKLMNOPQRSTWUVXYZ"
    symbol="!@#$%^&*()_-+=}]{[|\:;?/>.<,~`"
    count=0
    string=""
    for index in range(length): 
      count=count+1
      arch=random.choice(choice)
      c=random.choice(chars)
      s=random.choice(symbol)
      n=random.choice(num)
      C=random.choice(c_chars)
      if arch == "num":
         string=string+n
      elif arch == "symbol":
         string=string+s
      elif arch == "c_chars":
          string=string+C
      else:
         string=string+c
    return string
     
def Autofill(dtype):
    global queuefull
    import random as rd
    status=True
    if queuefull==False:
        match dtype:
            case 0:
                upperbound=int(input(" Enter Max Value:"))
                lowerbound=int(input(" Enter Min Value:"))
            case 1:
                upperbound=int(input(" Enter Max Length:"))
                lowerbound=int(input(" Enter Min Length:"))     
        while True:
            match dtype:
                case 0:
                    data=rd.randint(lowerbound,upperbound)
                case 1:
                    data=random_string(upperbound,lowerbound)
            if Enqueue(data)==False:
                break
    else:
        status=False
    return status

def sort():
    global queue,startpointer,nextfreepointer,freeslots,queuefull,queueempty
    counter=startpointer
    array=[]
    for index in range(len(queue)-freeslots):
        array.append(queue[counter])
        counter+=1
        if counter==len(queue):
            counter=0
    import random
    method=int(input("ENTER ALGORITHM TO SORT [0] BUBBLE | [1] INSERTION :"))
    match method:
        case 0:
            UpperBound=len(array)
            count=0
            swapcount=0
            passes=0
            while True:
                swaps=False
                count=count+1
                for index in range(UpperBound-count):
                    passes+=1
                    if array[index]>array[index+1]:
                        temp=array[index]
                        array[index]=array[index+1]
                        array[index+1]=temp
                        swaps=True
                        swapcount+=1
                if swaps==False:
                    break
##            print(f"swaps={swapcount}|pass={passes}")
##            for index in range(len(array)):
##                print(f"[{index+1}|{array[index]}]")
        case 1:
            passes=0
            swapcount=0
            for count in range(1,len(array)):
                passes+=1
                if array[count-1] > array[count]:
                    index=count
                    inplace=False
                    while index >= 1 and inplace == False:
                        temp=array[index]
                        array[index]=array[index-1]
                        array[index-1]=temp
                        swapcount+=1
                        if array[index-1] > array[index]:
                            inplace==True
                        else:
                            index-=1
##            print(f"swaps={swapcount}|pass={passes}")               
##            for index in range(len(array)):
##                print(f"[{index+1}|{array[index]}]")
    return array

def binary_search(searchdata,dtype):
    s_queue=sort()
##    for index in range(len(s_stack)):
##        print(s_stack[index])
    if dtype==0:
        searchDat=int(searchdata)
    else:
        searchDat=searchdata
    lowerBound=0
    upperBound=len(s_queue)
    while upperBound > lowerBound:
        mid=(lowerBound+upperBound)//2
        if s_queue[mid] > searchDat:
            upperBound=mid-1
        elif s_queue[mid] < searchDat:
            lowerBound=mid+1
        else:
            return True
    return False

def search(data,dtype):
    method=int(input("ENTER ALGORITHM TO SEARCH [0] BINARY | [1] LINEAR :"))
    match method:
        case 0:
            return binary_search(data,dtype) 
        case 1:
            global queue,startpointer,freeslots
            counter=startpointer
            array=[]
            for index in range(len(queue)-freeslots):
                array.append(queue[counter])
                counter+=1
                if counter==len(queue):
                    counter=0
            index=0
            while True:
                arraydata=array[index]
                if arraydata==data:
                    return True
                else:
                    index+=1
            return False
                    
            
            
                
    
    

def main():
    global dtype,queuedefined
    queuedefined=False
    while True:
        choice=getcommand()
        match choice:
            case 0:
                initialize_queue()
                print(" QUEUE DEFINED ")
            case 1:
                while True:
                        match dtype:
                            case 0:
                                try:
                                    data=int(input("Enter Data to Enqueue:"))
                                    break
                                except:
                                    print("PLEASE ENTER THE VALID QUEUE DATA TYPE: INT")
                            case 1:
                                data=input("Enter Data to Enqueue:")
                                break
                if Enqueue(data)== True:
                    print("DATA ADDED TO THE QUEUE")
                else:
                    print("ERROR:QUEUE FULL| UNABLE TO ADD DATA")
            case 2:
                stat,data=Dequeue(datatype)
                if stat==True:
                    print(f"{data} | ITEM DEQUEUED")
                else:
                    print(" QUEUE EMPTY ")
            case 3:
                veiw_unordered()
            case 4:
                veiw()
            case 5:
                s_data=input("ENTER SEARCH DATA: ")
                if search(s_data,dtype)==True:
                    print(f"{s_data} present in Queue")
                else:
                    print("-DATA NOT FOUND")
            case 6:
                if Autofill(dtype)== False:
                    print("ERROR - QUEUE ALREADY FULL ")
                else:
                    print(" QUEUE AUTOFILL COMMENCED ")
            case 7:
                break
                


                            
                    

main()
            
            
    
    
