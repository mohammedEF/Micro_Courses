while True: # to give the user multiple tries untill they enter a strong password
    password = input("Enter a password to check its strength: ")

    # checking against password rules
    is_long_enough = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)

    # display the results
    print("\nPassword Strength Check Results:")
    print(f"- Length (at least 8 characters): {'Passed' if is_long_enough else 'Failed'}")
    print(f"- At least one uppercase letter: {'Passed' if has_uppercase else 'Failed'}")
    print(f"- At least one lowercase letter: {'Passed' if has_lowercase else 'Failed'}")
    print(f"- At least one number: {'Passed' if has_number else 'Failed'}")

    # overall password strength
    if is_long_enough and has_uppercase and has_lowercase and has_number:
        print("\nYour password is strong!")
        break
    else:
        print("\nYour password is weak. Please try again.")