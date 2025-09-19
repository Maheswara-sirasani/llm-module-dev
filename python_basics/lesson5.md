## Python data structures

   These are the building blocks to store and organize the data

## Strings

common string operations

```python
s="Python"
print(len(s))
print(s.upper())
print(s[0])
print(s[-1])
print(s[1:4])
print("tho" in s)


output :

6
PYTHON
P
n
yth
True
```


### simple task
```python
st=input("enter a string")
print(st.upper())
print(st.lower())
print(st[::-1])

vowels='aeiouAEIOU'
vowel_count=sum(1 for char in st if char in vowels)
print("number of vowels",vowel_count)


output :


enter a stringAEIOUaeioumatlab
AEIOUAEIOUMATLAB
aeiouaeioumatlab
baltamuoieaUOIEA
number of vowels 12
```
