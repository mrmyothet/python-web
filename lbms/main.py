from tools import view_book,add_book,remove_book,edit_book
from db import books


print("_____Welcome_____")
print("1. View Book ")
print("2. Add Book")
print("3. Remove Book")
print("4. Edit Book")
print("5. Exit")  


while True:
    opt = int(input("Enter your choice: "))
    if opt == 1:    
        view_book(books)
    elif opt == 2:
        add_book(books) 
    elif opt == 3:
        remove_book(books)
    elif opt == 4:
        edit_book(books)
    elif opt == 5:
        print("Thanks for using")
        break
    else:
        print("Invalid input")

