import psycopg2

def connect():
    return psycopg2.connect(
        dbname = 'canteen_automation', 
        host = 'localhost', 
        user= 'postgres', 
        password= 'postgres', 
        port = '5434'
    )

def create_user(role_id, username, password, email, contact_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (role_id, username, password, email, contact_number) VALUES (%s, %s, %s, %s, %s)',(role_id, username, password, email, contact_number))
    conn.commit()
    cursor.close()
    conn.close()
    print('new user created successfully.')

def view_users():
    db = connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users ORDER BY user_id')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_user(user_id, username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET username=%s, password= %s WHERE user_id = %s', (username, password, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    print('user updated successfully.')

def delet_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE user_id = %s', (user_id))
    conn.commit()
    cursor.close()
    conn.close()

# execute the functions
# create_user(1, 'myothet', 'myothet', 'mr.myothet@gmail.com', '09964557349')
# read_users()
# update_user(1, 'mrmyothet', 'mrmyothet')

def main():
    print('1. Add user')
    print('2. View user')
    print('3. Update user')
    print('4. Delete user')

    opt = 0
    while opt != "5":
        opt = input("Enter option number : ")

        if opt == "1":
            role_id = 1
            name = input("Enter user name : ")
            password = input("Enter password : ")
            email = input("Enter email : ")
            contact_number = input("Enter contact number : ")
            create_user(role_id, name, password, email, contact_number)
        elif opt == "2":
            view_users()
        elif opt == "3":
            user_id = input("Enter user id to update : ")
            username = input("Enter updated name : ")
            password = input("Enter updated password : ")
            update_user(user_id, username, password)
        elif opt == "4":
            user_id = input("Enter the user id you want to delete: ")
            delet_user(user_id)
            print("user with user_id", user_id, "successfully deleted.")

main()