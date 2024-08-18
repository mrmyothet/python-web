email = "test@test.com"

if '@' in email and '.' in email:
    at_index = email.index('@')
    dot_index = email.index('.')

    if dot_index > at_index:
        print("Valid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")