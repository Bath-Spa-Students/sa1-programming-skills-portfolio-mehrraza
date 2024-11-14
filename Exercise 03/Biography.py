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

#  Explain variables for personal information
name = "RaZa"  # Name as a string
hometown = "Pakistan"    # Hometown as a string
age = 19                 # Age as an integer

# collect information in a dictionary with descriptive keys
info = {
    "Name": name,        # Key "Name" with the value of name
    "Hometown": hometown, # Key "Hometown" with the value of hometown
    "Age": age            # Key "Age" with the value of age
}

# Print each piece of information on a new line
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")