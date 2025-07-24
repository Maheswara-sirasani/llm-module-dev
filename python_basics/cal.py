def cal():
    print("select operator")
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    
    choice=input("enter choice")
    if choice in ('1','2','3','4'):
        num1=float(input("enter number 1 :"))
        num2=float(input("enter number 2 :"))
        if choice=='1':
            print("sum of numbers is :",num1+num2)
        elif choice=='2':
            print("substraction is :",num1-num2)
        elif choice=='3':
            print("multiplication is :",num1*num2)
        elif choice=='4':
           if num2!=0:
               print("division is :",num1/num2)
               
    else:
       print("inavlid input")
    
cal()            
       
        
                
        
          
    
        