st=input("enter a string")
print(st.upper())
print(st.lower())
print(st[::-1])

vowels='aeiouAEIOU'
vowel_count=sum(1 for char in st if char in vowels)
print("number of vowels",vowel_count)