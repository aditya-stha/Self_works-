def initialize_queue(length):
    global queue,freeslots
    queue=structure()
    freeslots=length

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

def getcommand():
    while True:
        print("[                1 - Enqueue | 2 - Dequeue          ]")
        print("[     3 - VEIW         | 4 - SEARCH  | 5 - AUTOFILL ]")
        print("[                          6 - END                  ]")
        command=int(input("ENTER COMMAND:"))
        if command > 0 and command < 7:
              break
        else:
            print("INVALID COMMAND")
    return command

def Enqueue(data):
    global queue,freeslots
    status=True
    if freeslots!=0:
        queue.insert(data)
        freeslots-=1
    else:
        status=False
    return status


def Dequeue(datatype):
    global queue,freeslots
    status=True
    if freeslots != 0 :
        Dequeued_record = queue.head
        queue.head=Dequeued_record.ref
        freeslots+=1
    else:
        Dequeued_record=None
        status=False
    return status,Dequeued_record

def veiw():
    global queue
    queue.printlinkedlist()
    
        
        
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
    global queue,freeslots
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
            Enqueue(data)
    else:
        status=False
    return status
            
        
def main():
    length=int(input("Enter Queue Size:"))
    initialize_queue(length)
    print("-CIRCULAR QUEUE INITIALIZED-")
    while True:
        choice=getcommand()
        match choice:   
            case 1:
                data=input("Enter Data to Enqueue:")           
                if Enqueue(data)== True:
                    print("DATA ADDED TO THE QUEUE")
                else:
                    print("ERROR:QUEUE FULL| UNABLE TO ADD DATA")
            case 2:
                stat,data=Dequeue()
                if stat==True:
                    print(f"{data.data} | ITEM DEQUEUED")
                else:
                    print(" QUEUE EMPTY ")
            case 3:
                veiw()
            case 4:
                global queue
                data=input("Enter Data to Search: ")
                node,status,empty=queue.search(data)
                if empty==False:
                    if node == None and status == True:
                        item=queue.head
                    elif status== True and node != None:
                        item=node.ref
                    else:
                        print(" DATA NOT IN LIST")
                        
                    print(f"{item.data} is Present in Queue ")
                else:
                    print(" LIST IS EMPTY ")
            case 5:
                if AutoFill()== False:
                    print("ERROR - QUEUE ALREADY FULL ")
                else:
                    print(" QUEUE AUTOFILL COMMENCED ")
            case 6:
                break
                


                            
                    

main()
            
            
    
    
