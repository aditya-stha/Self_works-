from platform   import system as system_name  
from subprocess import call   as system_call
import os

def extract_name(lineoftext):
    dataline=lineoftext
    data=dataline[2:]
    name=""
    for index in range(len(data)):
        if data[index]=="|":
            break
        else:
            name=name+data[index]
    return name

def linear_search():
    while True:
      choices=False
      filename=get_filename()
      file=open(filename,"r")
      search_data=input("Enter Name")
      while not choices:
          lineoftext=file.readline().strip()
          if lineoftext!="":
             data=extract_name(lineoftext)
             if search_data==data:
                 print("VALID DATA")
                 file.close()
          else:   
              print("INVALID DATA")
              file.close()
              break
            
          choice=input(" Do you want to SEARCH more data in this File ? [Y/N] : ")
          if choice=="N":
            clear_screen()
            choices=True
            
      choice=input(" Do you want to append any other file ? [Y/N] : ")
      if choice=="N":
         clear_screen()
         break
      
    
def clear_screen():
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    system_call([command])
    
def appendfile():
   while True:
      filename=get_filename()
      file=open(filename,"a")
      index=int(get_last_index(filename))
      while True:
         index = index + 1 
         name=input(" Enter Name: ")
         age=input(" Enter Age: ")
         lineoftext=str(index)+"."+name+"|"+age+"\n"
         file.write(lineoftext)
         clear_screen()
         choice=input(" Do you want to enter more data in this File ? [Y/N] : ")
         if choice=="N":
            clear_screen()
            break
      choice=input(" Do you want to append any other file ? [Y/N] : ")
      if choice=="N":
         clear_screen()
         break
      
      
def get_last_index(filename):
   prev=""
   file=open(filename,"r")
   while True:
      lineoftext=file.readline().strip()
      if lineoftext!="":
         prev=lineoftext
      else:
         break
   if prev == "":
      return 0
   else:
      index=prev[0]
      return index

def list_DIR():
   try: 
       file=open("DIR_FILE_LIST","r")
       while True:
          lineoftext=file.readline()
          if lineoftext=="":
             file.close()
             break
          else:
             print(" ",lineoftext)
   except:
       print(" ERROR: DIR FILE NOT DEFINED ")
       while True:
        press=input("Press [X] to Defined DIR file: ")
        if press=="X":
            break
       define_dir()
       print(" DIR DEFINED | CURRENT NO FILE TO LIST ")
       while True:
        press=input("Press [X] to create file: ")
        if press=="X":
            break
       createfile()
    
def get_filename():
   list_DIR()
   while True:
      search_index=int(input(" Enter File Name Index: "))
      file=open("DIR_FILE_LIST","r")
      while True:
         lineoftext=file.readline().strip()
         if lineoftext!="":
            if int(lineoftext[0])==search_index:
               n=lineoftext.strip()
               name=n[2:]
               file.close()
               return name
         else:
            break
      print(" [INVALID FILE INDEX]")
         

def createfile():
   filelist=open("DIR_FILE_LIST","a")
   filename=input(" Enter File Name: ")
   index = str(int(get_last_index("DIR_FILE_LIST"))+1)
   newfile=open(filename,"w")
   filelist.write(index+"."+filename+"\n")
   newfile.close()
   filelist.close()
   clear_screen()
   print(" [TASK COMPLETED]")

def printfile():
   filename=get_filename()
   file=open(filename,"r")
   while True:
      lineoftext=file.readline()
      if lineoftext!="":
         print(lineoftext)
      else:
         print(" [TASK COMPLETED]")
         break

def updatedata():
    while True:
                filename=get_filename()
                while True:
                    valid = False
                    while not valid:
                        file=open(filename,"r")
                        search_data=input("Enter Name to Update: ")
                        while True:
                            lineoftext=file.readline().strip()
                            if lineoftext!="":
                                 data=extract_name(lineoftext)
                                 if search_data==data:
                                     print("VALID DATA")
                                     valid= True
                                     file.close()
                                     break
                                     
                            else:
                                print("INVALID DATA")
                                file.close()
                                break
                    decoy=open("Decoy.txt","w")
                    NewDataName=input("Enter New Name to Replace:")
                    NewDataAge=input("Enter New Age to Replace:")
                    file=open(filename,"r")
                    while True:
                        lineoftext=file.readline().strip()
                        if lineoftext!="":
                            data=extract_name(lineoftext)
                            if search_data==data:
                                string=lineoftext[0:2]+NewDataName+"|"+NewDataAge+"\n"
                                decoy.write(string)
                            else:
                                decoy.write(lineoftext+"\n")
                        else:
                            break
                    file.close()
                    decoy.close()
                    os.remove(filename)
                    os.rename("Decoy.txt",filename)
                    
                    if input(f"Want to Update More Names in file {filename} [Y/N]: ")=="N": break
                if input("Want to Update in Another File [Y/N]: ")=="N": break

def deletedata():
    while True:
                filename=get_filename()
                while True:
                    valid = False
                    while not valid:
                        file=open(filename,"r")
                        search_data=input("Enter Name to Delete: ")
                        while True:
                            lineoftext=file.readline().strip()
                            if lineoftext!="":
                                 data=extract_name(lineoftext)
                                 if search_data==data:
                                     print("VALID DATA")
                                     valid= True
                                     file.close()
                                     break
                                     
                            else:
                                print("INVALID DATA")
                                file.close()
                                break
                    decoy=open("Decoy.txt","w")
                    file=open(filename,"r")
                    datapassed=False
                    while True:
                        lineoftext=file.readline().strip()
                        if lineoftext!="":
                            data=extract_name(lineoftext)
                            if search_data==data:
                                datapassed=True
                            if datapassed == False:
                                decoy.write(lineoftext+"\n")
                            elif datapassed == True and data!=search_data:
                                n=str(int(lineoftext[0])-1)
                                print(n)
                                string=n+lineoftext[1:]
                                decoy.write(string+"\n")
                        else:
                            break
                    file.close()
                    decoy.close()
                    os.remove(filename)
                    os.rename("Decoy.txt",filename)
                    
                    if input(f"Want to Delete More Names in file {filename} [Y/N]: ")=="N": break
                if input("Want to delete in Another File [Y/N]: ")=="N": break

def deletefile():
    while True:
        filename=get_filename()
        decoy=open("Decoy.txt","w")
        file=open("DIR_FILE_LIST","r")
        datapassed=False
        while True:
            lineoftext=file.readline().strip()
            if lineoftext!="":
                data=lineoftext[2:]
                if filename==data:
                    datapassed=True
                if datapassed == False:
                    decoy.write(lineoftext+"\n")
                elif datapassed == True and data!=filename:
                    n=str(int(lineoftext[0])-1)
                    string=n+lineoftext[1:]
                    decoy.write(string+"\n")
            else:
                break
        file.close()
        decoy.close()
        os.remove("DIR_FILE_LIST")
        os.rename("Decoy.txt","DIR_FILE_LIST")
        os.remove(filename)
        if input("Want to Delete More Files [Y/N]: ")=="N": break
    
def bubblesort():
    while True:
        filename=get_filename()
        file=open(filename,"r")
        array=[]
        sorttype=int(input(" Sort Alphabetically to Name [0] | Sort Numerically to Age [1] "))
        while True:
            lineoftext=file.readline().strip()
            if lineoftext != "":
                        array.append(lineoftext[2:])   
            else:
                break
        file.close()
        UpperBound=len(array)
        count=0
        while True:
            swaps=False
            count+=1
            for index in range(UpperBound-count):
              match sorttype:
                case 0:
                    if array[index]>array[index+1]:
                        temp=array[index]
                        array[index]=array[index+1]
                        array[index+1]=temp
                        swaps=True
                case 1:
                    current=array[index]
                    upcomming=array[index+1]
                    if current[len(current)-3:len(current)] > upcomming[len(upcomming)-3:len(upcomming)]:
                        temp=array[index]
                        array[index]=array[index+1]
                        array[index+1]=temp
                        swaps=True 
            if swaps==False:break
        decoy=open("Decoy.txt","w")
        for index in range(len(array)):
            string=str(index+1)+"."+array[index]
            decoy.write(string+"\n")
        decoy.close()
        os.remove(filename)
        os.rename("Decoy.txt",filename)
        if sorttype==0:
            print("File Sorted Alphabetically")
        else:
            print("File Sorted Numerical to Age")
        if input("Want to Sort Another File [Y/N]:")=="N":break


def menu():
   print(" [ 0: List Files in DIR | 1: Create File | 2: Print File ] ")
   print(" [ 3: Linear Search FF  | 4: Append File | 5: UpdateData ] ")
   print(" [ 6: Delete Data  FF   | 7: Delete File | 8: Bubble Sort] ")
   print(" [                          9:Quit PROG                  ] ")
   while True :
    choice=int(input(" Option [ ]: "))
    if choice >-1 and choice < 10 :
        return choice
    else:
        clear_screen()
        print(" ERROR 101 INVALID INPUT")
        
def define_dir():
    global dirdefined
    file=open("DIR_FILE_LIST","w")
    file.close()
    dirdefined=True

def main():
    while True:
            choice=menu()
            match choice:
                   case 0:
                       clear_screen()
                       list_DIR()
                       #list files in dir
                   case 1:
                       clear_screen()
                       createfile()
                       #create a file
                   case 2:
                       clear_screen()
                       printfile()
                       #print file
                   case 3:
                       clear_screen()
                       linear_search()
                       #find data from a file
                   case 4:
                       clear_screen()
                       appendfile()
                          #add data to a file
                   case 5:
                       clear_screen()
                       updatedata()
                       #update data to a file
                   case 6:
                       clear_screen()
                       deletedata()
                       #delete data from a file
                   case 7:
                       clear_screen()
                       deletefile()
                       #delete a file
                   case 8 :
                       clear_screen()
                       bubblesort()
                       
                    #bubble sort a file

                   case 9 :
                       break

main()                      #end program
while True:
    username=input(" Enter Username:" )
    password=input(" Enter Password:" )
    if password == "1234":
                clear_screen()
                print(" [ USER AUTHENCIATED ]  ")
                main()
                break
    else:
        clear_screen()
        print(" INVALID CREDITENTIALS ")
            

            





    
