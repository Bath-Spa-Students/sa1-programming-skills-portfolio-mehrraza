# This is the function to check if a number is even or odd
def check_even_odd(number):
    #Checking if the number is evenly divisible by 2.
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # If it's not, it's odd
        return f"{number} is odd."

#this is the main function to handle user input and display the result
def main():
    # This is to ask the user to enter a number
    try:
        user_number = int(input("Please enter a number: "))
        # This is to call the check_even_odd function and get the result message
        result_message = check_even_odd(user_number)
        # This is to print the result message
        print(result_message)
    except ValueError:
        # This is to check if the user enters a non-integer value, display an error message
        print("Invalid input. Please enter a numerical value.")

# This only runs the main function if this script is run directly
if __name__ == "__main__":
    main()
