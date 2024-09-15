subjects = ["Myanmar", "English", "Maths", "Chemistry"]
# Adding data to list

# append
print(subjects)
subjects.append("Physics")

# insert
subjects.insert(1, "Science")
print(subjects)

# print(f"After modifying: {subjects}")

# pop
result = subjects.pop(1)
print(result)
print(subjects)

# remove
subjects.remove("Myanmar")
# subjects.remove("myanmar")

# index
index = subjects.index("English")
print(index)

# clear
subjects.clear()
print(subjects)

# usecase - buffer space - temporary storage
nums = [1, 2, 3, 4, 5]
processed_data = []
for i in nums:
    processed_data.append(i * 2)

print(processed_data)

# copy
copied_list = nums.copy()
print(copied_list)

copied_list = nums[::]
print(copied_list)

# count

# extend
students = ["John", "James", "Chris"]
new_students_today = ["Harry", "Felix", "Max"]
# students.append(new_students_today)
print(students)
# ['John', 'James', 'Chris', ['Harry', 'Felix', 'Max']]

# students.extend(new_students_today)
print(students)
# ['John', 'James', 'Chris', 'Harry', 'Felix', 'Max']

for new_student in new_students_today:
    students.append(new_student)

print(students)

students.reverse()
print(students)

students = ["John", "James", "Chris", "Paul", "Andrew"]
# students.sort()
print(students)
# ['Andrew', 'Chris', 'James', 'John', 'Paul']

students.sort(key=len)
print(students)
