def fact(f_num):
    num=f_num
    num_f = 1
    count = 1
    while True:
     num_f=num_f*count
     count = count+1
     if count > num:
         break
    return num_f

def Binomial_Expansion():    
    prob=0
    ps=float(input("Probability of successive event: "))
    pn=1-ps
    n=int(input("Total Tries: "))
    e=int(input("X=" ))
    comb= ((fact(n))/(fact(e)*(fact(n-e))))
    jk=(((ps)**e)*((pn)**(n-e)))
    print("P(",e,") = ", (comb*jk))

def Ap_MT():
    prob=0
    N=int(input("Enter Number of Attempts: "))
    p=float(input("Probability of Success: "))
    pn=1-p
    E=int(input("Probability of event happening atleast N times ? N :"))
    for index in range (E,N+1):
        comb = ((fact(N))/(fact(index)*(fact(N-index))))
        exp =(((p)**index)*((pn)**(N-index)))
        prob=prob+(comb*exp)
        j=str(E)
    print("P(X>="+j+")=",prob)

def Ap_LT():
    prob=0
    N=int(input("Enter Number of Attempts: "))
    p=float(input("Probability of Success: "))
    pn=1-p
    E=int(input("Probability of event happening less than N times ? N :"))
    for index in range (0,E):
        comb = ((fact(N))/(fact(index)*(fact(N-index))))
        exp =(((p)**index)*((pn)**(N-index)))
        prob=prob+(comb*exp)
        j=str(E)
    print("P(X<"+j+")=",prob)

def Var_E():
    n=int(input("Enter Total Attempts:"))
    p=float(input("Probability of Success: "))
    pn=1-p
    Var=str(n*p*pn)
    E=str(n*p)
    print("Var(X)="+Var+", E(X)="+E)
    


    

def menu():
   while True :
    mode=int(input("1:Binomial expansion | 2: Aprrox Atleast \n"
                    "3: Aprrox less than | 4: Var(X) & E(x)| 0 : end | [ ] :"))
    match mode:
        case 1:
            Binomial_Expansion()
        case 2:
            Ap_MT()
        case 3:
            Ap_LT()
        case 4:
            Var_E()
        case 0:
            print("SEE YA ")
            break

menu()
