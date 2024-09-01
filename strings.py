name = "BoBoMin"

# string indexing
first_char = name[0]
second_char = name[1]
last_char = name[6]

# reverse indexing
last_char = name[-1]
char_before_last = name[-2]

print(first_char)
print(second_char)
print(last_char)
print(char_before_last)

size = len(name)

last_index = size - 1 
last_char = name[last_index]
print('last index', last_char)

# slicing 
name = technortal = "Technortal"
# start_index
# end_index
# step 
nor = name[4:7:1]
print(nor)

step_2 = name[0:4:2]
print(step_2)

# tech = name[0:4]
tech = name[:4]
print(tech)

nortal = name[4:]
print(nortal)

copy_name = name[:]
print(copy_name)

reverse_copy = name[::-1]
print(reverse_copy)