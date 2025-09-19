def cal():
    print("select operators")
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    choice=input("enter u r choice")
    
    if choice in('1','2','3','4'):
        num1=float(input("enter u num1  "))
       
        num2=float(input("enter number 2  "))
        if choice=='1':
             print("result :",num1+num2)
       
        elif choice=='2':
             print("result :",num1-num2) 
        elif choice=='3':
             print("result :",num1*num2) 
        elif choice=='4':
            if num2!=0:
             print("result :",num1/num2)
    else:
        print("invalid option")  
        
cal()                    