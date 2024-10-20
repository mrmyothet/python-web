from library.library import Library
from users.registration import register_user
from users.login import login_user
from library.book import Book

def main():
    lib = Library()

    # User Registration
    user_name = input("Please, enter user name: ")
    password = input("Please, enter your password: ")
    register_user(lib, user_name, password)

    # User Login
    login_user(lib, user_name, password)

    # Add a new book
    new_book = Book(1, "Python Programming", "Mark Lutz", '978-0596158101')
    lib.add_book(new_book)
    
    new_book = Book(2, "Python Cookbook", "David Beazley & Brian K. Jones", "978-1449340377")
    lib.add_book(new_book)

    # List books
    for book in lib.list_books():
        print(book)


if __name__ == '__main__':
    main()
