# programming
# variable
# naming conventions
# naming rules
# -> reserved words (def, if, elif, break, continue)
# data type -> number(integer,float), string, boolean
# static typing / dynamic typing   # general knowledge

# built-in functions
# -> print() -> display the data at console or output interface
# -> type()  -> return the typed value of data
# -> len()   -> return the length or size of data
# -> input() -> accept the value from console and return into a variable
# -> int()   -> convert string value to integer value
# -> float() -> convert int/str value to float value
# -> list()  -> type casting / from iterable objects to list
# -> sum()   -> do addition like itertion
# -> range() -> generator functions

# opeators
# -> arithemetic operators (add,sub,mul,div)
# -> comparison operators
# -> logical operators

# string structure
# -> string indexing
# -> slicing
# -> string concatenation
# -> printing with f-string


#  List
# list structure
# list indexing
# list slicing
# list methods


# conditional statement
# - if / else
# - if / elif / else

# conditional expression
# statement vs expression

# iteration statement
# - looping with for loop
# - looping with while loop
# - range() generator function


# Function
# Built-in Functions Vs User-defined Functions

# Input -> Process -> Output (Return / Non-Return)

# Process
# Input -> Process


# def func_name(parameter):
#     implementation
#     return value


def len_copy(container):
    length = 0
    for _ in container:
        length += 1

    return length


lst = [1, 2, 3, 4, 5]
result = len_copy(lst)
print(result)


def sum_copy(container):
    sum = 0

    for item in container:
        sum += item

    return sum


result = sum_copy(lst)
print(result)


def area(width, length=5):
    return width * length


result = area(width=3, length=3)
print(result)

result = area(width=3)
print(result)
