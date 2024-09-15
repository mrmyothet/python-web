# List
# Tuple
# Dictionary
# Set

days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
print(type(days_of_week))

# memory efficient
# mutable vs immutable
# performance


# List -> Mutable -> Editable items inside of the container object
# Sring, Tuple -> Immutable

name = "Technortal"

# name[0] = "S"
# TypeError: 'str' object does not support item assignment

print(name)
name_lowercase = name.lower()

print(name_lowercase)
print(name)


# memory efficient

import sys

# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tpl1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst1 = [1, 2, 3, 4, 5]
tpl1 = (1, 2, 3, 4, 5)

size1 = sys.getsizeof(lst1)
size2 = sys.getsizeof(tpl1)

print(size1, size2)

# tuple packing

# function return
books = books = ["Python Book", "Java Book", "C++ Book", "C Book", "Go lang Book"]
for book in enumerate(books):
    print(book)
    print(type(book))


index = days_of_week.index("Monday")
print("index :" + str(index))

count = days_of_week.count("Monday")
print("count :" + str(count))
