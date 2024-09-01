# Database
user_name = "KyawKyaw"
password = "KoKyawGyi"

name = input("Enter user name : ")


# if name == user_name and pwd == password: 
#     print("Login succesful")
# else: 
#     print("Invalid Credential")

if name == user_name: 
    pwd = input("Enter password : ")
    if pwd == password:
        print("Login Successful.")
    else:
        print("Password is invalid.")
else:
    print("User doesn't exist.")