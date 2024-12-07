from app.db import get_db


def create_user(username, password, email):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)",
            (username, password, email),
        )
        db.commit()
