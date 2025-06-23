def initialize(datatype,stacklength):
    global stack,freepointer,toppointer,stackfull,stackdefined
    stack=[datatype for index in range (stacklength) ]
    freepointer=0
    toppointer=-1
    stackfull=False
    stackdefined=True

def pop():
    global stack,freepointer,toppointer,stackfull,dtype
    status=True
    match dtype:
        case 0:
            data=0
        case 1:
            data="" 
    if freepointer > 0 :
        temp=data
        data=stack[toppointer]
        stack[toppointer]=temp
        toppointer=toppointer-1
        freepointer=freepointer-1
        stackfull=False
        return (status,data)
    else:
        status=False
        return (status,data)
           

def push(data):
    global stack,freepointer,toppointer,stackfull
    status=True
    if stackfull == False:
        stack[freepointer]=data
        toppointer +=1
        freepointer +=1
        if freepointer == len(stack):
            stackfull=True
    else:
        status=False
    return status
    
    
    

def veiw():
    global stack,freepointer,toppointer
    print("STACK CONTENT")
    freeslots= len(stack)-freepointer
    if toppointer != (len(stack)-1):
        print(f"[ NEXT FREE SLOT: {freepointer+1} | TOP POINTER: {toppointer+1} | FREE SLOTS: {freeslots} ]")
    else:
        print(f"[ STACK CURRENTLY FULL | TOP POINTER : {toppointer+1} ]")
    
    for index in range(len(stack)):
        data=stack[index]
        print(f"[ {index+1} | {data} ]")
        
def search_linear(searchdata):
    global stack,freepointer,dtype
    index=0
    if dtype==0:
        searchDat=int(searchdata)
    else:
        searchDat=searchdata
    while True:
        data=stack[index]
        if data==searchDat:
            return True
        index+=1
        if index==len(stack):
            return False
def sort():
    global stack,dtype,freepointer
    if dtype==0:
        init_data=0
    else:
        init_data=""
    array=[init_data for index in range(freepointer) ]
##    print(" UNSORTED LIST ")
    for index in range(freepointer):
        array[index]=stack[index]
##        print(f"[ {index+1} | {array[index]} ]")
    import random
    method=random.randint(0,1)
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
                    
            
            
        
    
def binary_search(searchdata):
    s_stack=sort()
##    for index in range(len(s_stack)):
##        print(s_stack[index])
    global dtype
    if dtype==0:
        searchDat=int(searchdata)
    else:
        searchDat=searchdata
    lowerBound=0
    upperBound=len(s_stack)
    while upperBound > lowerBound:
        mid=(lowerBound+upperBound)//2
        if s_stack[mid] > searchDat:
            upperBound=mid-1
        elif s_stack[mid] < searchDat:
            lowerBound=mid+1
        else:
            return True
    return False
  

def getchoice():
    print(" [0] INITIALIZE STACK | [1] PUSH | [2] POP | [3] VEIW")
    print(" [4] SEARCH LINEAR    | [5] SEARCH BINARY  | [6] AUTOFILL ")
    print("                           [7] END                        ")
    while True:
        choice=int(input("Enter Choice:"))
        if choice > -1 and choice < 8:
            break
        else:
            print("INVALID INPUT [0-7]")
    return choice

def AutoFill():
    import random as rd
    global stack,dtype,freepointer,toppointer,stackfull
    status=True
    if stackfull==False:
        if dtype==0:
            upperbound=int(input(" Enter Max Value:"))
            lowerbound=int(input(" Enter Min Value:"))
            for index in range(freepointer,len(stack)):
                data=rd.randint(lowerbound,upperbound)
                stack[index]=data
        else:
            upperbound=int(input(" Enter Max Length:"))
            lowerbound=int(input(" Enter Min Length:"))
            for index in range(freepointer,len(stack)):
                data=random_string(upperbound,lowerbound)
                stack[index]=data

        toppointer=len(stack)-1
        stackfull=True
        freepointer=len(stack)
    else:
        status=False
    return status
        
        
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
    

def main():
    global stackdefined,dtype,freepointer,toppointer,stackfull
    stackdefined=False
    while True:
        choice=getchoice()
        match choice:
            case 0:
                print(" [0] INTEGER | [1] STRING " )
                while True:
                    dtype=int(input("Enter STACK DATA TYPE:"))
                    if dtype ==0:
                        datatype=0
                        break
                    elif dtype==1:
                        datatype=""
                        break
                    else:
                        print("INVALID DATA TYPE")    
                stacklength=int(input("ENTER STACK LENGTH:") )
                initialize(datatype,stacklength)
            case 1:
                data=input("Enter Data item []: ")
                if dtype== 0 : data=int(data)
                if push(data)== True:
                    print("- TASK SUCCESSFUL " )
                else:
                    print("- STACKOVERFLOW")
            case 2:
                stat,data=pop()
                if stat==True:
                   print(f"POPPED ITEM = {data} " )
                else:
                    print(" STACK EMPTY ")
            case 3:
                veiw()
            case 4:
                data=input("Enter Data item to search []: ")
                if search_linear(data) == True:
                    print("DATA FOUND ")
                else:
                    print("DATA NOT FOUND")
            case 5:
                data=input("Enter Data item to search []: ")
                if binary_search(data)== True:
                    print("DATA FOUND")
                else:
                    print("DATA NOT FOUND")
            case 6:
                if AutoFill()== False:
                    print("ERROR - STACK ALREADY FULL ")
                else:
                    print(" STACK AUTOFILL COMMENCED ")
            case 7:
                
                break
                
                
main()


