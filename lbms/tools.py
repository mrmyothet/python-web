# Program Controller Functions


# def view_book(books):
#     print("Book List")
#     for index, book in enumerate(books):
#         print(f"{index + 1} : {book}")


def view_book(books):
    if len(books) == 0:
        print("No books available")
        return

    print(
        "{:<10}{:<30}{:<20}{:<15}".format(
            "Book Id", "Title", "Author", "Published Year"
        )
    )
    print("_" * 75)

    for book_id, details in books.items():
        print(
            "{:<10}{:<30}{:<20}{:<15}".format(
                book_id,
                details.get("title"),
                details.get("author"),
                details.get("published_year"),
            )
        )


# def add_book(new_book, books):
#     books.append(new_book)
#     print("Book is added successfully.")
def add_book(books):
    book_id = input("Enter book ID : ")
    if book_id in books:
        print("Book with this ID already exists.")
    else:
        title = input("Enter book title : ")
        author = input("Enter author name : ")
        published_year = input("Enter published year : ")
        new_book = {"title": title, "author": author, "published_year": published_year}
        books[book_id] = new_book
        print("New book is successfully added")


# def remove_book(book_name, books):
#     books.remove(book_name)
#     print("Book is removed successfully.")


# def remove_book(books):
#     book_id = 0
#     book_name = input("Enter book name to remove : ")
#     for id, details in books.items():
#         # print(id, details)
#         if details.get("title") == book_name:
#             book_id = id

#     if book_id == 0:
#         print("Book not found")
#     else:
#         del books[book_id]
#         print(book_name, "is removed successfully")


def remove_book(books):
    book_id = input("Enter book id to remove : ")
    if book_id in books:
        del books[book_id]
        print("Book removed successfullly")
    else:
        print("Book not found ")


# def edit_book(book_num, new_book_name, books):
#     books[book_num] = new_book_name
#     print("Book is added successfully.")


def edit_book(books):
    book_id = input("Enter the book id to edit : ")
    if book_id in books:
        title = input("Enter new title : ")
        author = input("Enter new author name : ")
        published_year = input("Enter published year : ")
        books[book_id] = {
            "title": title,
            "author": author,
            "published_year": published_year,
        }
        print("Book has been updated.")
