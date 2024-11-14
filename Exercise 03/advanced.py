# Encourage the user to enter their full name, removing any extra whitespace
username = input("Enter your full name: ").strip() # .strip() Removes extra spaces around input

# inspire the user to enter their hometown, removing any extra whitespace
userhometown = input("Enter your hometown: ").strip() # .strip() Removes extra spaces around input

# request the user for their age in a loop to ensure valid input
while True:
    try:
        # Converting the input to an integer
        userage = int(input("Enter your age: "))
        break  # Exit the loop if conversion is successful
    except ValueError:
        # to print an error if input is not a valid integer
        print("Invalid input. Please enter a numerical value for age.")
        # to print the collected information
print("\nUser Information:")
print(f"Name: {username}")
print(f"Hometown: {userhometown}")
print(f"Age: {userage}")