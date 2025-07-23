## Control flow

1. Descision Making Statements

## Part A

If
Elif
Else


## If Condition
 
 Do something

## Elif condition

do something else

## else 

Fallback

## simple program

```python

age=int(input("enter your age : "))

if age>18:
    print("you are major")
elif age==18:
    print("you are just become an major")
else:
    print("your are minor")    


output :

enter your age : 18
you are just become an major

enter your age : 25
you are major


enter your age : 7
your are minor


```

## Task 1
```python

marks=int(input("enter your marks"))
if marks>=90:
    print("a grade")
elif marks>80 and marks<90 :
    print("b grade") 
elif marks>70 and marks<80 :
    print("c grade")   
elif marks>60 and marks<70 :
    print("d grade") 
else :
    print("fail")

output :


enter your marks  55
fail

enter your marks  89
b grade

```

## Part B 
 For and While loops

```python

# for loop example

for i in range(1,6):
    print(i)


output : 

1
2
3
4
5
```

```python

# while loop
count = 1
while count <=5 :
    print(count)
    count +=1

output : 


1
2
3
4
5
```

## Task

```python
n=int(input("enter n value"))
for i in range(1,10):
    print(f"{n}*{i}={n*i}")

output :

 enter n value9
9*1=9
9*2=18
9*3=27
9*4=36
9*5=45
9*6=54
9*7=63
9*8=72
9*9=81
```
## task

count 10 to 1

```python

count=10
while count > 0:
    print(count)
    count -=1

output:
10
9
8
7
6
5
4
3
2
1
```
for n input revrse order
```python  
n=int(input("enter number:  "))
while n>0:
    print(n)
    n-=1      
```

