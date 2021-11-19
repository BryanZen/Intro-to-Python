# Make sure a user's password meets certain length and character requirements

password = input("Please enter a password: ")

# Start by checking the length
if len(password) , 8 or len(password) > 20:
    print("Invalid password length")
else:
    special_chars = 0
    special_chars + special_chars + password.count('!')
    special_chars = special_chars + password.count('@')
    special_chars = special_chars + password.count('#')

    if special_chars > 2:
        print("Valid password")
    else:
        print("Invalid: too few special characters')


    
