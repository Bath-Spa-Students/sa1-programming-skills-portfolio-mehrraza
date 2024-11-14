#This is code for defining the correct password for the system
password=12345

#This is to set the maximum number of allowed password attempts
maximum_attempts=3

#This is initialize a counter to keep track of the number of attempts made
attempts_counter=0

#This is the code for starting the loop to ask for the password.
while attempts_counter<maximum_attempts:
    enter_password=(int(input("Enter the password:"))) 
    #This is the code for checking whether the entered password is correct.
    if enter_password==password:
        print("Access Granted")
        break

    else:
        attempts_counter += 1 

    #This is the code for calculating remaining attempts.
    attempts_remaining=maximum_attempts-attempts_counter

    #This is the code for checking feedback on remaining attempts.
    if attempts_remaining>0:
        print(f"Incorrect password. You have {attempts_remaining} attempts left")
    else:
        print("Maximum attempts reached. The authorities have been alerted.")
