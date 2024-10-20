class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = {}

    def add_book(self, new_book):
        self.books.append(new_book)

    def remove_book(self, id):
        return [book for book in self.books if book.id != id]
    
    def find_book(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def list_books(self):
        return self.books
    
    def add_user(self, user_name, password):
        if user_name in self.users:
            print("User already exists.")
        else:
            self.users[user_name] = password

    def login(self, user_name, password):
        if user_name in self.users and self.users[user_name] == password:
            print(f"Welcome {user_name}")
            return True
        else:
            print("Login Failed")
            return False