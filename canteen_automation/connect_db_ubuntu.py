# sudo apt-get install libpq-dev
# sudo apt-get install python3-dev
# pip install psycopg2

import psycopg2

conn = psycopg2.connect(
    dbname="canteen_automation",
    user="myothet",
    password="myothet",
    host="localhost",
    port="5432",
)

print(conn)

# cursor = conn.cursor()
# cursor.execute("INSERT INTO roles (role_name) VALUES ('Staff')")
# conn.commit()
