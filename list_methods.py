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
subjects.remove("Myanamr")
subjects.remove("myanmar")

# index
index = subjects.index("English")
print(index)
