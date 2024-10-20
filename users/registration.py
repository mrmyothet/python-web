from library.library import Library

def register_user(library, user_name, password):
    library.add_user(user_name, password)