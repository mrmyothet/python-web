students = ['John', 'Harry', 'Jame', 'Felix', 'Kin']
print(students)

# list with first 3 students
first_3_students = students[0:3]
print("first 3 students : ", first_3_students)

# list with last 3 students 
last_3_students = students[:1:-1]
print("last 3 students : ", last_3_students)

# last student 
length = len(students)
last_student = students[length - 1]
print("Last student : ", last_student)

# third student 
third_student = students[3]
print("third student : ", third_student)

# student list with reverse order 
reverse_students = students[::-1]
print("reverse_students : ", reverse_students)

# copy list except the first student 
copy_list_ex_first_student = students[1:]
print("copy list except the first student : ", copy_list_ex_first_student)