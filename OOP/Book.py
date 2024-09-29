class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + " : " + self.author

book_1 = Book("Clean Code", "Uncle Bob")
print(book_1)