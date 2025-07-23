## Operators 

## Types Of Operators

1. Arithmatic operators ('+",'-','*','/','//','%','**')
2. Comparsion operators (==,!=,<,>,<=,>=)
3. Logical operators( and ,or , not)
4. Assignment operators (=,+=,-=,*=,etc)



## simple example

```python

  a = 10
  b = 3

  #arithmatic

  print("addition",a+b)
  print("floor division",a//b)
  print("substraction",a-b)
  print("multilpication",a*b)
  print("division",a/b)
  print("percentage",a%b)
  print("mul",a**b)

  #logical
  print("a>b:",a>b)


  #logical

  x=True
  y=False
  print("x and y:",x and y)
  print("x or y:",x or y)
  print("not x:",not x)


  output : 
           addition 13
           floor division 3
           substraction 7
           multilpication 30
           division 3.3333333333333335
           percentage 1
           mul 1000
           a>b: True
           x and y: False
           x or y: True
           not x: False
```

## Task

Python program to analyze all arithmatic and logical operators

```python

a=int(input("enter a value :"))
b=int(input("enter b value :"))

# arithmatic

print("sum : ",a+b)
print("differnce : ",a-b)
print("product : ",a*b)
print("division : ",a/b)
print("module : ",a%b)
print("power : ",a**b)

# comparision

print("a==b :",a==b)
print("a!=b :",a!=b)
print("a>b :",a>b)
print("a<b :",a<b)


output : 


enter a value :70
enter b value :5
sum :  75
differnce :  65
product :  350
division :  14.0
module :  0
power :  1680700000
a==b : False
a!=b : True
a>b : True
a<b : False

