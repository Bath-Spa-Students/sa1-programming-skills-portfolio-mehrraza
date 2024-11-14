# This is a predefined list of names to search from
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This is the prompt the user to enter a name they want to look up, removing any extra spaces
search_term = input("Please enter the name you're looking for: ").strip()

# This is to check if the entered name exists in the list, using a case-insensitive search
if search_term.lower() in [name.lower() for name in names]:
    # This is to check if the name is found, provide a friendly success message
    print(f"Good news! '{search_term}' is in the list.")
else:
    # This is to  print if the name is not found, let the user know in a friendly way
    print(f"Sorry, '{search_term}' isn't in the list.")


    # these are the list of names to search through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This is the prompt the user to enter the name they are looking for, trimming any extra spaces
search_name = input("Please enter the name you want to search for: ").strip()

# This is the flag to track whether the name is found during the search
found = False

# This is the loop through each name in the list to check if it matches the user's input
for name in names:
    # This is to convert both names to lowercase to ensure the search is case-insensitive
    if name.lower() == search_name.lower():
        # This is to check if a match is found, set 'found' to True and inform the user
        found = True
        print(f"Great news! '{search_name}' is in the list.")
        break  # This is to exit the loop early since we found the name

# This is to check if the loop completes and the name wasn't found, let the user know
if not found:
    print(f"Sorry, '{search_name}' is not in the list.")