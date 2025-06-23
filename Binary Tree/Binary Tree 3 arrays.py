def initialize_tree(length,Type):
    global Data , Rpointer , Lpointer , Free , Root
    match Type:
        case 0:
            init_data=0
        case 1:
            init_data=""

    Data = [ init_data for index in range(length) ]
    Rpointer = [ None for index in range(length) ]
    Lpointer = [ None for index in range(length) ]
    for index in range (length):
        Lpointer[index]=index+1 # creating linked list of free nodes in tree
        
    Lpointer[-1]=None
   

    Free=0 # first item of free list  
    Root=None # tree empty
    print("Tree Initialized")

def veiw():
    global Data , Rpointer , Lpointer , Free , Root
    print(f" Free Pointer = {Free} | Root Pointer = {Root} ")
    for index in range(len(Data)):
        print(f" {index} | {Rpointer[index]} | {Data[index]} | {Lpointer[index]} ")
    
    

def add_data(data):
    global Data , Rpointer , Lpointer , Free , Root
    # check is list is full                
    # if not full add data to free spot on the free list
    # if the binary is empty this new spot is where the root points
    # if not link the spot to the correct position to add
    if Free!= None:
        New=Free
        Free=Lpointer[Free]
        if Data[New] == 0 : data  = int(data)
        Data[New]=data   # adding data to free  and breaking it from the free list 
        Lpointer[New]=None
        if Root != None:
            Current = Root
            direction=""
            found = False
            
            while not found:
                if data > Data[Current]:
                    if Lpointer[Current] ==None:
                        found = True
                        direction="L"
                    else:
                        Current = Lpointer[Current]
                else:
                    if Rpointer[Current] == None:
                        found = True
                        direction="R"   
                    else:
                        Current = Rpointer[Current]
                        
            match direction:
                case "L":
                    Lpointer[Current]=New
                case "R":
                    Rpointer[Current]=New
        else:
            Root = New
        return True
    else:
        return False
    
def traverse(current):
    global Data , Rpointer , Lpointer , Free , Root
    if current == None:
        return
    Rside = Rpointer[current]
    Lside =  Lpointer[current]
    if Rside != None:
        traverse(Rside)
    print(Data[current])
    if Lside != None:
        traverse(Lside)
        
    
    
    
        
def main():
    while True:
        print(" [0] Initialize | [1] Veiw | [2] Add Data | [3] Traverse | [4] Break ")
        command=int(input("Enter Command:"))
        match command:
            case 0:
                length=int(input("Enter Max Data Count:"))
                Type=int(input("Enter Data Type [ 0 - Numeric | 1 - String ]:"))
                initialize_tree(length,Type)
            case 1:
                veiw()
            case 2:
                data=input("Enter Data to Add")
                if add_data(data) == False:
                    print("Error: Data Slots Full")
                else:
                    print(" Data Added ")
            case 3:
                global Root
                traverse(Root)
            case 4:
                break
main()
                        
                
                    
                        
                    
  
