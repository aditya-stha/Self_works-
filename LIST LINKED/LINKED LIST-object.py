class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        item=node(data)
        if self.head is None:
            self.head=item
        else:
            currentitem=self.head
            while True:
                if currentitem.ref is None:
                    currentitem.ref=item
                    break
                currentitem=currentitem.ref
            
    def printlinkedlist(self):
        currentnode=self.head
        print("[head] -->",end=" ")
        while currentnode is not None:
            print(f"[{currentnode.data}] -->",end=" ")
            currentnode=currentnode.ref
        print("None")

    def search(self,data):
        currentnode=self.head
        prevnode=None
        empty=True
        while currentnode is not None:
            empty=False
            if currentnode.data == data:
                return prevnode,True,empty
            prevnode=currentnode
            currentnode=currentnode.ref
        return prevnode,False,empty
        

    def delete(self,data):
        prevnode,status= self.search(data)
        if  status != False:
            if prevnode==None:
                currentnode=self.head
                nextnode=currentnode.ref # if the removing from the head
                self.head=nextnode
            else:
                currentnode=prevnode.ref
                nextnode=currentnode.ref # if removing from other parts
                prevnode.ref=nextnode
            return True
        else:
            return False
    
    
            

def main():

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
            ll=linkedlist()
            print("LINKED LIST DEFINED")
        case 1:
            try:
                    value=input("Enter data to Link:")
                    ll.insert(value)
                    print(" VALUE LINKED ")
                    ll.printlinkedlist()
                    
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                ll=linkedlist()
                print("LINKED LIST DEFINED")
        case 2:
            try:
                data=input("Enter data to Unlink:")
                if ll.delete(data) == False:
                    print("EMPTY LINKED LIST // DATA NOT VALID")
                else:
                    print(" DATA UNLINKED")
                    ll=linkedlist()
                    
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                ll=linkedlist()
                print("LINKED LIST DEFINED")
        case 3:
            try:
                ll.printlinkedlist()     
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                ll=linkedlist()
                print("LINKED LIST DEFINED")
        case 4:
            data=input("Enter Data to Search: ")
            node,status,empty=ll.search(data)
            if empty==False:
                
                if node == None and status == True:
                    item=ll.head
                elif status== True and node != None:
                    item=node.ref
                else:
                    print(" DATA NOT IN LIST")
                    
                print(f"{item.data} is Present in Linked List")
            else:
                print(" LIST IS EMPTY ")
        case 5:
            break
                 
main()
        

