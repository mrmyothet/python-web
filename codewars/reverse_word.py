def reverse_words(text):
    lst = text.split(" ")
    rev_lst = []
    result = ""
    for item in lst:
        rev_lst.append(item[::-1])

    for item in rev_lst:
        result += item + " "

    return result.rstrip()


print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))
