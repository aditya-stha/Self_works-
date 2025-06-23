def sorter():
    global data,order
    end=findend()
    array=[]
    for index in range(end+1):
        array.append(data[index])

    array=sort(array,order)
    
    for index in range(end+1):
        data[index]=array[index]

def sort(array,f):
    for index in range(1,len(array)):
        match style:
            case 0:#ascending
                if array[index] < array[index-1]:
                    count=index
                    place=False    
                    while count >=1 and place==False:
                                temp=array[count]
                                array[count]=array[count-1]
                                array[count-1]=temp
                                if array[count-1] > array[count-2]:
                                    place==True
                                else:
                                    count-=1
            case 1:#dscending
                if array[index] > array[index-1]:
                    count=index
                    place=False    
                    while count >=1 and place==False:
                                temp=array[count]
                                array[count]=array[count-1]
                                array[count-1]=temp
                                if array[count-1] > array[count-2]:
                                    place==True
                                else:
                                    count-=1
        
    return array
                            
    
def findend():
    global ref
    index=0
    while True:
        if ref[index]==None:
            break
        else:
            index+=1
    endindex=index

    return endindex
    
def pushdown():
    global data
    end=findend()#returns the index of the list whose ref is none
    for index in range(end,-1,-1):
        data[index+1]=data[index]
        
##    for index in range(len(data)):
##        if index < (len(data)-1):
##            data[index+1]=data[index]
##        
    for index in range(len(data)):
        print(data[index])

def pushup():
    global data
    end=findend()#returns the index of the list whose ref is none
    for index in range(len(data)-1):
        
        data[index]=data[index+1]
        
##    for index in range(len(data)):
##        if index < (len(data)-1):
##            data[index+1]=data[index]
##        
    for index in range(len(data)):
        print(data[index]) 
        
def link(linkdata):
## link  by  order<needs to be initizalized at the begining>
## link in after a certain element by request < required to display the data list >
## link to the begining / end
    global data,ref,listorder,order,freeslots,dtype
    if dtype==0: linkdata=int(linkdata)
    status=True
    if freeslots!=0:
        #only if there is space left in the list
        if freeslots==len(data):
                    #starting the list theres no start end or between
                    data[0]=linkdata
                    ref[0]=None#its the end of the data list
        else:
            match listorder:
                case 0:#Sequential
                    # just adding the data to the end of the list and sorting it easy way
                    end=findend()
                    data[end+1]=linkdata
                    ref[end+1]=None
                    ref[end]=end+1
                    sorter()
                case 1:#Random
                    Type=int(input(" [0] Link to Start | [1] Link to End | [2] Link Between <index_Upper> and <index_Lower>: "))
                    match Type:
                        case 0:
                            #link to start
                            pushdown()#shifts the whole data array to make space for the new data
                            data[0]=linkdata
                            end=findend()
                            ref[end+1]=None
                            ref[end]=end+1
                            ref[0]=1
                        case 1:
                            #link to end
                            end=findend()
                            data[end+1]=linkdata
                            ref[end+1]=None
                            ref[end]=end+1
                        case 2:
                            # link to between , get the indexes , shift everything down onestep starting from lower index 
                            veiw()
                            end=findend()
                            while True:
                                index_u=int(input("Enter <index_Upper> : "))
                                index_l=int(input("Enter <index_Lower> : "))
                                if index_l > index_u:
                                    break
                                else:
                                    print("INVALID INDEX ENTRY")
                            for index in range(index_l,end+1):
                                data[index+1]=data[index]
                            # the current data in the l index replaced by new data & the ref of the new end
                            data[index_l]=linkdata
                            ref[end]=end+1
                            ref[end+1]=None
        freeslots-=1                          
    else:
        status=False
    return status
            
            


def search(searchDat):
    global data,dtype
    
    if dtype==0:searchDat=int(searchDat)
    
    end=findend()
    array=[data[index] for index in range(end+1)]
    for index in range(len(array)):
        print(array[index])
        
    array=sort(array,0)
    
    for index in range(1):
        print(array[index])
        
    lowerBound=0
    upperBound=len(array)
    while upperBound >= lowerBound:
        mid=int((lowerBound+upperBound)/2)
        if array[mid] > searchDat:
            upperBound=mid-1
        elif array[mid] < searchDat:
            lowerBound=mid+1
        else:
            return True
    return False
    
def getref(s_data):
    
    global data,dtype
    if dtype==0: s_data=int(s_data)
    found = False
    index=0
    while not found:
        if data[index]==s_data:
            found=True
        else:
            index+=1

    return index


def unlink(s_data):
    global data,ref,listorder,freeslots,datatype
    choice=int(input("Enter Choice: [0] By Data , [1]Head, [2]Tail: "))
    match listorder:
        case 0:
            end=findend()
            match choice:
                case 0:
                    while True:
                        if search(s_data) == True:
                            break
                        else:
                            print("invalid data")
                    pointer=getref(s_data)
                    data[pointer]=datatype      
                case 1:
                    data[0]=datatype
                    sorter()
                    data[end]=datatype
                case 2:
                    data[end]=datatype
                    
            ref[end-1]=None
            if freeslots==0:
                ref[end]=None
            else:
                ref[end]=end+1
            sorter()      
        case 1:
            end=findend()
            match choice:
                case 0:
                    while True:
                        if search(s_data) == True:
                            break
                        else:
                            print("invalid data")
                    pointer=getref(s_data)
                    for index in range(pointer,len(data)-1):
                        data[index]=data[index+1]
                    data[end]=datatype
                case 1:
                    pushup()
                    data[end]=datatype
                case 2:
                    data[end]=datatype
            
            ref[end-1]=None
            if freeslots== 0:
                ref[end]=None
            else:
                ref[end]=end+1
    freeslots+=1
                    
            
## unlink for 3 possible options , unlink by data , unlink first , unlink last
    
def initialize():
    global data,ref,listorder,order,freeslots,datatype,dtype
    dtype=int(input("Enter Data list Data type [0] integer [1] string:"))
    length=int(input("Enter Linked List Max Size: "))
    match dtype:
        case 0:
            datatype=0
        case 1:
            datatype=""
            
    print("Enter the Order for the List to be Managed: ")
    listorder=int(input("[0] SEQUENTIAL [1] RANDOM: "))
    if listorder==0:
        order=int(input("[0] Ascending [1] Descending: "))
    data=[ datatype for index in range (length)]
    ref=[ index+1 for index in range(length) ]
    ref[-1]=None
    freeslots=length
    
def printfreelist():
    global data,ref
    for index in range(len(data)):
        print( f" {index}[  {str(data[index])} | {ref[index]} ]")
        
    

def printlist():
    global data,ref,freeslots
    print("start-->",end="")
    for index in range (len(data)-freeslots):
        print(f"{str(data[index])}-->",end="")
    print("None")

def veiw():
    global data,ref
    end=findend()
    for index in range(end+1):
        print( f" index= {index}[ data= {str(data[index])} | pointer= {ref[index]} ]")

def main():
 global freeslots,data
 while True:
    while True:
        print("[ 0 - initialize list | 1 - Link Data | 2 - Unlink Data]")
        print("[  3 - Veiw List      |   4- SEARCH   | 5 - END        ]")
        command=int(input("Enter Choice:"))
        if command > -1 and command < 6:
            break
        else:
            print("INVALID COMMAND")
        
    match command:
        case 0:
            initialize()
            print("LINKED LIST DEFINED")
            printfreelist()
        case 1:
            try:
                if freeslots == 0:
                    print(" LINKED LIST FULL")
                else:
                    value=input("Enter data to Link:")
                    link(value)
                    print(" VALUE LINKED ")
                    printlist()
                    
                printfreelist()
                    
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
                print("LINKED LIST DEFINED")
        case 2:
            try:
                if freeslots==len(data):
                    print("LINKED LIST EMPTY")
                else:
                    data=input("Enter data to Unlink:")
                    unlink(data)
                    print(" DATA UNLINKED")
                    printlist()

                printfreelist()
                    
                    
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
                print("LINKED LIST DEFINED")
        case 3:
            try:
                printlist()     
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
                print("LINKED LIST DEFINED")
            printfreelist()
        case 4:
            data=input("Enter Data to Search: ")
            status=search(data)
            if freeslots!=0:
                
                if status==False:
                    print(" DATA NOT IN LIST")
                else: 
                     print(f"{data} is Present in Linked List")
            else:
                print(" LIST IS EMPTY ")
            printfreelist()
        case 5:
            break
        
                 
main()
printfreelist()
        
    
    

