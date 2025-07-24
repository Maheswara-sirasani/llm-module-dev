def sum_digits(number):
    total=0
    while number>0:
        digit=number%10
        total+=digit
        number//=10
    return total

num=int(input("enter a digit number"))
print("sum of digit number is :",sum_digits(num))    
    
    