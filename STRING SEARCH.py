#gaining input data
string_a=input("Enter The Main String:") 
string_b=input("Enter The Sub which you want to locate:")
#initializing variables
store_c="" 
count=0
found=False
#string search loop

for index in range (len(string_a)):
   char_a=string_a[index]#extraction of individual characters 
   if char_a==string_b[count]: # store it if the characters matche
    store_c=store_c+char_a
    count=count+1
    #streak=streak+1 #continuos streak of matching characters 
    if store_c==string_b:
        print (f"[{string_a}] contains [{string_b}] thus: true")
        found=True
        break
   else:
    store_c="" #refresh the stored data and re initialize variables 
    streak=0
    count=0
if found==False:
    print(f"[{string_a}] doesnt contain [{string_b}] thus: False") 


   
