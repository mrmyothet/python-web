# import controllers
# controllers.view_book

# from lbms.tools import *

from tools import view_book, edit_book, add_book, remove_book
from db import books

# run_trigger = True

# while run_trigger:
while True:
    print("")
    print("_____Welcome_____")
    print("1. View ")
    print("2. Add ")
    print("3. Remove ")
    print("4. Edit ")
    print("5. Exit")
    opt = int(input("Enter your choise : "))

    # View Book
    if opt == 1:
        # print("_____Book List_____")
        # print(books)
        # for index, book in enumerate(books):
        #     print(f"{index+1} : {book}")
        # controllers.view_book(books)
        view_book(books)

    # Add Book
    if opt == 2:
        add_book(books)
        # new_book = input("Enter name of the new book : ")

        # if new_book in books:
        #     print("book is already existed in the list")
        # else:
        #     add_book(new_book, books)
        # books.append(new_book)
        # print(new_book + " is added successfully to the book list. ")

        # print(books)
        # for index, book in enumerate(books):
        #     print(f"{index+1} : {book}")

    # Remove Book
    if opt == 3:
        remove_book(books)

        # result = books.remove(remove_book)
        # if result != None:
        #     print("There is no book with name : " + remove_book)

        # print(remove_book + " is removed from the book list")

        # print(books)
        # for index, book in enumerate(books):
        #     print(f"{index+1} : {book}")

    # Edit Book
    if opt == 4:
        # index = int(input("please, provide book number your want to edit. : "))
        # book_name = input("Please, Enter book name you want to update : ")
        # edit_book(index - 1, book_name, books)
        edit_book(books)

    if opt == 5:
        # run_trigger = False
        break

print("I hope you enjoy using the program. Bye Bye!")
