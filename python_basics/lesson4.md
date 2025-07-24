## Functions in python

functions wiil help organise a code and reuse code
if we define a function we call it when we are required

## part 1 

1. defining and using python

```python 
def greet(name):
    print("hello",name)

greet("mahesh")


output :
  

  hello mahesh
```
## with return
```python

def add(a,b):
    return a+b

result = add(3,4)
print("sum is :",result)  

output :
 
 sum is : 7
```
## Task

```python
def area_of_circle(radius):
    return(3.14*radius*radius)

area=area_of_circle(88)
print("area of circle is :",area)


output :

area of circle is : 24316.16
```
## task 
even number function
```python
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

output :

enter a number  34039875432987543287541
odd number


enter a number  4
even number
```

### task
```python
# simple program to do calculations in calculator
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
       
        
 output :

 select operator
1. addition
2. substraction
3. multiplication
4. division
   enter choice2
   enter number 1 :789
   enter number 2 :90
   substraction is : 699.0  
```
## Part B
## Recursion (Function Calling Itself)   

Example:
```python
def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)
print(factorial(5))        
        
output:  120
```
## simple program fiboncci number at given position
```python
def fab(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
    
position=6
print("position of faboncci is :",position,"value is",fab(position))    
    

    output :
    position of faboncci is : 6 value is 8
```
## simple program to sum of digits

```python

def sum_digits(number):
    total=0
    while number>0:
        digit=number%10
        total+=digit
        number//=10
    return total

num=int(input("enter a digit number "))
print("sum of digit number is :",sum_digits(num))    
    
    
output :

enter a digit number 123456789
sum of digit number is : 45
