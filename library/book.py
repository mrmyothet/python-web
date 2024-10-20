class Book:
    def __init__(self,id, title, author, ISBN) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.isbn = ISBN

    def __str__(self):
        return self.title + " : " + self.author