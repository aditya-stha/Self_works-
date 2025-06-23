

def proper_veiw():
    global data,ref,head
    print(" Head-->",end=" ")
    index=head
    while True and index!=None:
        print(f"{data[index]}-->",end=" ")
        index=ref[index]
    print("None",end=" \n")
    
def initialize(length):
    global data,ref,NumofFreeSlots,freeindex,head
    data = [ 0 for index in range (length) ] # Integer For Data side of the Node
    ref = [ index+1 for index in range(length)]# Integer For Pointer side of the Node
    ref[-1]=None
    freeindex=0
    head=None

def veiw_raw():
     global data,ref
     for index in range(len(data)):
         print(f" {index} - {data[index]} | {ref[index]} ")

def link(linkdata):
    global data,ref,freeindex,head
    # take the next free slot,
    #add data to it ,
    #look in the data list ,
    #find its position ,
    #put it there


    data[freeindex]=linkdata
    newIndex=freeindex
    freeindex=ref[freeindex]
    currentIndex = head
    # when can the current index be none : 1 when the is no data in the list and 2 when the data list is at its end
    
    while currentIndex != None and linkdata > data[currentIndex]:
        previndex=currentIndex
        currentIndex=ref[currentIndex]
        
    if currentIndex==head:
        head=newIndex
    else:
        ref[previndex]=newIndex
    ref[newIndex]=currentIndex

    
def search(s_data):
    global data,ref,head
    index=head
    found=False
    while not found and index!=None:
        if data[index]==s_data:
            return True,prev
        else:
            prev=index
            index=ref[index]
    return found,0
    

def unlink(unlinkdata):
     global data,ref,freeindex,head
     if head!= None:
        current=head
        while current!=None and unlinkdata!=data[current]:
            prev=current
            current=ref[current]
        if current==None:
                print(f"{unlinkdata} not present in list")
                return False
        elif current==head:
                head=ref[current]
        else:
                ref[prev]=ref[current]
        data[current]=0
        ref[current]=freeindex
        freeindex=current
        return True
     else:
        print("LIST EMPTY")
        return False
            
         


def main():
    while True:
        print("[ 0-INITIALIZE | 1 - RAW VEIW | 2- LINK | 3 - UNLINK |4 - P.VEIW | 5 - BREAK ]")
        choice=int(input(" Enter Choice :")) #Integer to Indiacate Command
        match choice:
            case 0:
                length=int(input("Enter Length:"))
                initialize(length)
                print(" LINKED LIST INITIALIZE ")
            case 1:
                veiw_raw()
            case 2:
                global freeindex
                Linkdata=int(input("Enter Data to link:"))
                if freeindex!=None:
                    link(Linkdata)
                else:
                    print("LIST FULL")
            case 3:
                Unlinkdata=int(input("Enter Data to Unlink:"))
                unlink(Unlinkdata)
            case 4:
                proper_veiw()
            case 5:
                break
                

main()
