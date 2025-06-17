#Find Student and Display marks or else mention student not found.

dict = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Eve": 88
}

student_name = input("Enter the students name: ").capitalize()

if (student_name in dict):
    print("{}'s marks: {}".format(student_name.capitalize(),dict.get(student_name)))
else:
    print("Student not found.")