# Program Controller Functions

def view_book(books):
    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("{:<10}{:<30}{:<20}{:<15}".format('BookID','Title','Author','Published Year'))
        print("_"*90)
        for book_id, details in books.items():
            print("{:<10}{:<30}{:<20}{:<15}".format(book_id,details.get('title'),details.get('author'),details.get('published_year')))

def add_book(books):
    book_id = input("Enter book ID : ")
    if book_id in books:
        print("Book with this ID already exists.")
    else:
        title = input("Enter book title : ")
        author = input("Enter author name : ")
        published_year = input("Enter published year : ")
        book_data = {'title' : title, 'author' : author, 'published_year' : published_year}
        books[book_id] = book_data
        print("Book added successfully.")


def remove_book(books):
    book_id = input("Enter the book id to remove : ")
    if book_id in books:
        del books[book_id]
        print("Book removed successfully")
    else:
        print("Book not found!")

def edit_book(books):
    book_id = input("Enter the book id to edit : ")
    if book_id in books:
        title = input("Enter new title ")
        author = input("Enter new author name : ")
        published_year = input("Enter new publsihed year : ")
        books[book_id] = {'title' : title, 'author' : author, 'published_year' : published_year}
        print('Book is updated successfully!')
    else:
        print('Book not found')