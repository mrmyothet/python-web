# Program Controller Functions


def view_book(books):
    print("Book List")
    for index, book in enumerate(books):
        print(f"{index + 1} : {book}")


def add_book(new_book, books):
    books.append(new_book)
    print("Book is added successfully.")


def remove_book(book_name, books):
    books.remove(book_name)
    print("Book is removed successfully.")


def edit_book(book_num, new_book_name, books):
    books[book_num] = new_book_name
    print("Book is added successfully.")
