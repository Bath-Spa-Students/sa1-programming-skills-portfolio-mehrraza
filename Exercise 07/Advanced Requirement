# This is to define the correct password for the system
correct_password = "codelab1"

# This is to set the maximum number of attempts a user is allowed
max_attempts = 5

# This is to initialize a counter to track the number of attempts made by the user
attempts = 0

# This is to start a loop that will run until the correct password is entered or maximum attempts are reached
while attempts < max_attempts:
    # This is the prompt to the user to enter the password, with a message for guidance
    user_input = input("Please enter the password: ").strip()
    
    # This is for the increment the attempts counter by 1 after each entry
    attempts += 1

    # This is to check if the entered password matches the correct password
    if user_input == correct_password:
        # This is to check if the password is correct, grant access and stop the loop
        print("Access granted. Welcome User!")
        break
    else:
        # This is to calculate remaining attempts to inform the user
        remaining_attempts = max_attempts - attempts
        # This is to notify the user that the password is incorrect and display the remaining attempts
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        
        # This is to check if the user has reached the maximum allowed attempts, issue a final warning
        if attempts == max_attempts:
            print("Maximum attempts reached. Authorities have been alerted due to multiple failed access attempts.")
