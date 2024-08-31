books = ["Python Book", "Java Book", "C++ Book", "C Book", "Go lang Book"]

# run_trigger = True

# while run_trigger:
while True:
    print("")
    print("_____Welcome_____")
    print("1. View Book")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")
    opt = int(input("Enter your choise : "))

    if opt == 1:
        print("_____Book List_____")
        # print(books)
        for index, book in enumerate(books):
            print(f"{index+1} : {book}")

    if opt == 2:
        new_book = input("Enter name of the new book : ")
        if new_book in books:
            print("book is already existed in the list")
        else:
            books.append(new_book)
            print(new_book + " is added successfully to the book list. ")
            # print(books)
            for index, book in enumerate(books):
                print(f"{index+1} : {book}")

    if opt == 3:
        remove_book = input("Enter book name to remove : ")

        result = books.remove(remove_book)
        if result != None:
            print("There is no book with name : " + remove_book)

        print(remove_book + " is removed from the book list")
        # print(books)
        for index, book in enumerate(books):
            print(f"{index+1} : {book}")

    if opt == 4:
        # run_trigger = False
        break

print("I hope you enjoy using the program. Bye Bye!")
