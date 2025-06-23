class node:
    def __init__(self,data,ref):
        self.data=data
        self.ref=ref



def initialize(length):
    global dtype,array,head,FreeNode # to keep track of the data in different parts of the modules
    match dtype:
        case 0:
            init_data=0
        case 1:
            init_data=""
    dummy=node(init_data,None)
    array= [ node(init_data,None) for index in range(length)]
    for index in range(len(array)-2,-1,-1):
        array[index].ref=array[index+1] 
    array[len(array)-1].ref=None
    head=None
    FreeNode=array[0]

def linkDescend(data):
    global array,head,FreeNode,order
    if FreeNode!=None:
        NewNode=FreeNode
        FreeNode=FreeNode.ref
        NewNode.data=data
        CurNode=head   
        while CurNode!=None and data <  CurNode.data :
            PreNode=CurNode
            CurNode=CurNode.ref
        if CurNode==head:
            head=NewNode
        else:
            PreNode.ref=NewNode
        NewNode.ref=CurNode
        return True
    else:
        return False

def linkAscend(data):
    global array,head,FreeNode,order
    if FreeNode!=None:
        NewNode=FreeNode
        FreeNode=FreeNode.ref
        NewNode.data=data
        CurNode=head   
        while CurNode!=None and data >  CurNode.data :
            PreNode=CurNode
            CurNode=CurNode.ref
        if CurNode==head:
            head=NewNode
        else:
            PreNode.ref=NewNode
        NewNode.ref=CurNode
        return True
    else:
        return False
    
def delinkStart():
    global head,FreeNode
    item=head
    head=head.ref
    item.ref=FreeNode
    FreeNode=item
    
    
def delinkEnd():
    global head,FreeNode
    item=head
    while True:
        if item.ref == None:
            break
        else:
            prev=item
            item=item.ref
    prev.ref=None
    item.red=FreeNode
    FreeNode=item

def delinkbydata(data):
    global head,FreeNode
    item=head
    while True:
        if item.data == data:
            break
        else:
            prev=item
            item=item.ref
    prev.ref=item.ref
    item.red=FreeNode
    FreeNode=item
    
        
def printlist():
    global head
    print("start-->",end="")
    item=head
    while True:
        if item!=None:
         print(f"[ {item.data} ]-->",end="")
         item=item.ref
        else:
            break
    print("None")

def search(data):
    global head
    item=head
    while item!=None:
        if item.data == data:
            return True
        else:
            item=item.ref
    return False

def printfreelist():
    global array,head
    print(f"head={head.data}")
    for index in range(len(array)):
##        if array[index].data != None and array[index].ref!= None:
           print( f" {array[index]} | [  {(array[index].data)} | {array[index].ref} ]")
##        else:
##            print (f" {index} | [ {(array[index].data)} | None ]")
            
            
                        
def main():
    while True:
        while True:
              print("[ 0 - INITIALIZE | 1 - LINK | 2- UnLink | 3 - VEIW | 4- RAW.V| 5-SEARCH | 6-END ]")
              command=int(input("Enter Command:"))
              if command >=0 and command <= 6:
                  break
        match command:
            case 0:
                global dtype,order
                dtype=int(input("Enter Data Type: 1 - string | 0 - integer :"))
                order=int(input("Enter Order : 0 - Ascending | 1 - Descending :"))
                length=int(input("Enter Max Length:"))
                initialize(length)
                print("LIST INITIALIZED")
            case 2:
                global head
                if head!=None:
                    if head.ref!=None:
                        delink=int(input("DeLink - 0 - Head | 1 - End | 2 - by Data:"))
                        match delink:
                            case 0:
                                delinkStart()
                                print("deLINKED")
                            case 2:
                                delinkEnd()
                                print("deLINKED")
                            case 3:
                                data=int(input("Enter Data:"))
                                if search(data)==True:
                                    delinkbydata(data)
                                    print("deLINKED")
                                else:
                                    print("DATA NOT FOUND")
                    else:
                        delinkStart()
                        
                else:
                    print(" EMPTY ")
                            
                
            case 1:
                data=int(input("Enter Data:"))
                match order:
                    case 0:
                        status=linkAscend(data)
                    case 1:
                        status=linkDescend(data)
                if status==True:
                    print(" DATA LINKED ")
                else:
                    print("MAX LIMIT REACHED")
            case 3:
                printlist()
            case 4:
                printfreelist()
            case 5:
                data=int(input("Enter Data:"))
                if search(data)==True:
                    print(" DATA FOUND ")
                else:
                    print("DATA NOT FOUND")
            case 6:
                break
            
            
            

            

    
            
            

    

main()

    
        
    
