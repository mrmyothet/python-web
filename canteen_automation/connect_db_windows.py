import psycopg2

conn = psycopg2.connect(
    dbname="canteen_automation",
    user="postgres",
    password="admin123!",
    host="127.0.0.1",
    port="5432",
)

print(conn)

# cursor = conn.cursor()
# cursor.execute("INSERT INTO roles (role_name) VALUES ('Staff')")
# conn.commit()

cursor = conn.cursor()
query = "SELECT * FROM roles"
lst = cursor.execute(query)
rows = cursor.fetchall()
# conn.commit()

print(rows)
