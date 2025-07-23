def is_even(number):
    if number%2==0:
        return True
    else:
        return False
    
num=int(input("enter a number"))  
if is_even(num) :
    print("even number")
else:
    print("odd number")        
        