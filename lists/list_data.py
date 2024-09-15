students = ['Aung Aung', 'Maung Maung', 'Kyaw Kyaw', 32]
print(type(students))

# Indexing 
first_student = students[0]
second_student = students[1]
third_student = students[2]
room_number = students[3]
print(first_student, second_student, third_student, room_number)

#    print(first_student)    # IndentationError: unexpected indent

# print(fourth_student)       # NameError: name 'fourth_student' is not defined.

# index_error = students[4]   # IndexError: list index out of range

# Slicing 
# list[start:end:step]

students = ['Aung Aung', 'Maung Maung', 'Kyaw Kyaw', 32]
AgAgMgMg = students[0: 2]
print("students[0: 2]", AgAgMgMg)

copy_of_students = students[:]
print(copy_of_students)
print(students[1:])