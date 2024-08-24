counter = 5

correct_pin = "1234"

user_pin = ""

while user_pin != correct_pin and counter > 0:
    user_pin = input("Enter your pin number :")
    counter -= 1
