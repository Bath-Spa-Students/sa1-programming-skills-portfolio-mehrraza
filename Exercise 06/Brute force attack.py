# This code is to define the correct password for the system
correct_password = "12345"

# This is to set the maximum number of allowed password attempts
maximum_attempts = 3

# This is to initialize a counter to keep track of the number of attempts made
attempts = 0

# This is to start a loop that continues until the correct password is entered or attempts are exhausted
while attempts < maximum_attempts:
    # Ask the user to enter the password
    user_input = input("Please enter the password: ").strip()
    
    # This is to mask the entered password with asterisks for privacy
    masked_password = '*' * len(user_input)
    
    # This is to increase the attempt count by 1 after each entry
    attempts += 1

    # This is to check if the entered password matches the stored correct password
    if user_input == correct_password:
        # This is to check if correct, grant access and end the loop
        print("Access granted. Welcome User!")
        break
    else:
        # This is to check if incorrect, display an error message along with the masked password
        print(f"Incorrect password: {masked_password}")
        
        # This is to provide a hint if the user is on their second-to-last attempt
        if attempts == maximum_attempts - 1:
            print("Hint: The password is number.")
        
        # This is to check if the user has used all attempts, lock them out and notify them
        if attempts == maximum_attempts:
            print("Access denied. You have been locked out due to too many incorrect attempts.")
