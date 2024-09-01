books = ["Python Book", "Java Book", "C++ Book", "C Book", "Go lang Book"]

# append()
books.append


# pop() - not destroy
# pop(index)
result = books.pop()
print(result)
print(books)
result = books.pop(2)
print(result)
print(books)

# remove
result = books.remove("Java Book")
print(books)
