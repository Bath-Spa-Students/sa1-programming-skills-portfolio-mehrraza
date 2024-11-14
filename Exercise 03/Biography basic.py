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