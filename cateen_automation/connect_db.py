# pip install psycopg2

import psycopg2

# Server 
# Address IP : localhost / 127.0.0.1
# dbname
# user -> postgres
# password -> admin123!
# host 
# port 
# connection 
conn = psycopg2.connect(
    dbname = 'canteen_automation', 
    user = 'postgres', 
    password = 'postgres', 
    host = 'localhost', 
    port = '5434'
)

print(conn)