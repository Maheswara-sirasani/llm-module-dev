## create a dictionary to store students' names and their marks, then print the names and marks
students_marks = {
    "Alice": 85,            
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}               
for student, mark in students_marks.items():
    print(f"{student}: {mark}")
        