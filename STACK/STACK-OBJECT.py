
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class structure:
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
        print("head-->",end="")
        while currentnode is not None:
            print(f"[{currentnode.data}]-->",end="")
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
        prevnode,status,empty= self.search(data)
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
        
def push(data):
    global ll,freeslots
    status=True
    if freeslots!=0:
        ll.insert(data)
        freeslots-=1
    else:
        status=False
    return status
    
        
    
def pop():
    global ll,freeslots
    if ll.head is None:
            top=ll.head
    else:
            currentitem=ll.head
            while True:
                if currentitem.ref is None:
                    top=currentitem
                    break
                currentitem=currentitem.ref
    data=top.data            
    node,status,empty=ll.search(data)
    if empty==False:
                if node == None and status == True:
                    item=ll.head
                    data=item.data
                    ll.delete(data)
                    freeslots+=1
                    return True,data
                elif status== True and node != None:
                    item=node.ref
                    data=item.data
                    ll.delete(data)
                    freeslots+=1
                    return True,data
                else:
                    print(" DATA NOT IN LIST")
                    error=""
                    return False,error     
    else:
                print(" LIST IS EMPTY ")
                return False,error
def initialize():
    global ll,freeslots
    ll=structure()
    freeslots=int(input("ENTER STACK LENGTH:"))
    print("LINKED LIST DEFINED")

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

def AutoFill():
    import random as rd
    global ll,freeslots
    status=True
    if freeslots!=0:
        upperboundInt=int(input(" Enter Max Integer Value:"))
        lowerboundInt=int(input(" Enter Min Integer Value:"))
        upperboundst=int(input(" Enter Max String Length:"))
        lowerboundst=int(input(" Enter Min String Length:"))
        for index in range(freeslots):
            dtype=rd.randint(0,1)
            match dtype:
                case 0:
                    data=str(rd.randint(lowerboundInt,upperboundInt))
                case 1:
                    data=random_string(upperboundst,lowerboundst)
            push(data)      
    else:
        status=False
    return status

def main():
 global ll,freeslots
 while True:
    while True:
        print("[ 0 - initialize list | 1 - PUSH Data | 2 - POP  Data ]")
        print("[  3 - Veiw List      |   4- SEARCH   | 5 - AutoFill  ]")
        print("[                         6 - END                     ]")
        print()
        command=int(input("Enter Choice:"))
        if command > -1 and command < 7:
            break
        else:
            print("INVALID COMMAND")
        
    match command:
        case 0:
            initialize()
        case 1:
            try:
                value=input("Enter data to PUSH:")
                if push(value) ==True:
                    print(" DATA STACKED " )
                else:
                    print("STACK FULL")
                ll.printlinkedlist()
                    
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
        case 2:
            try:
                stat,dat=pop()
                if stat == True:
                    ll.printlinkedlist() 
                    print(f" POPPED ITEM = {dat}")
                else:
                    print("LIST EMPTY")
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
        case 3:
            try:
                ll.printlinkedlist()     
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
        case 4:
            try:
                data=input("Enter Data to Search: ")
                node,status,empty=ll.search(data)
                if empty==False:
                    
                    if node == None and status == True:
                        item=ll.head
                    elif status== True and node != None:
                        item=node.ref
                    else:
                        print(" DATA NOT IN LIST")
                        
                    print(f"{item.data} is Present in Stack")
                else:
                    print(" LIST IS EMPTY ")
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
        case 5:
            try:
                if AutoFill()==True:
                    print(" AUTO FILL COMMENCED ")
                else:
                    print(" STACK FULL ")
            except:
                print("ERROR - LIST UNDEFINED | AUTO DEFINITION INITIATED")
                initialize()
        case 6:
            break
                 
main()

    
    
    
    
