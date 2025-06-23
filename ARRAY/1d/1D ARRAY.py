# MyArray: ARRAY[LB:UB] OF DATATYPE

def initialize(length,datatype):
    global array
    match datatype:
        case 0:
            Initializing_data=0
        case 1:
            Initializing_data=""
    array=[ Initializing_data for index in range (length) ]

def view():
    global array
    for index in range( len(array)):
        print(f" {index} | {array[index]} ")

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

def entry(entrytype,datatype):
    global array
    match entrytype:
        case 0:
            for index in range(len(array)):
                data=input("ENTER DATA:")
                if datatype==0: data=int(data)
                array[index]=data
        case 1:
            match datatype:
                case 0:
                    maxi=int(input("MAXIMUM:"))
                    mini=int(input("MINIMUm:"))
                    import random as rd
                    for index in range(len(array)):
                        array[index]=rd.randint(mini,maxi)
                case 1:
                    maxi=int(input("MAXIMUM:"))
                    mini=int(input("MINIMUm:"))
                    for index in range(len(array)):
                        array[index]=random_string(maxi,mini)
                    

                        
                        
                
    
    
                
    

def main():
    length=int(input("ENTER ARRAY LENGTH: "))
    datatype=int(input("[0] FOR INTEGER | [1] FOR STRING"))
    initialize(length,datatype)
    view()
    entrytype=int(input(" ENTRY TYPE ? [0] MANUAL [1] AUTOMATIC: "))
    entry(entrytype,datatype)
    view()
    
    

main()
    
