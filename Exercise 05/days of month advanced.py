# This is a dictionary that links each month number (1-12) to the number of days in that month for a non-leap year
days_of_months = {
    1: 31,   # January has 31 days
    2: 28,   # February has 28 days (in a non-leap year)
    3: 31,   # March has 31 days
    4: 30,   # April has 30 days
    5: 31,   # May has 31 days
    6: 30,   # June has 30 days
    7: 31,   # July has 31 days
    8: 31,   # August has 31 days
    9: 30,   # September has 30 days
    10: 31,  # October has 31 days
    11: 30,  # November has 30 days
    12: 31   # December has 31 days
}

# This is to ask the user to enter a month number between 1 and 12
try:
    monthnumber = int(input("Please enter the month number (1-12): ").strip())  # Remove extra spaces around input

    # This is to check if the entered month number is within the valid range of 1 to 12
    if 1 <= monthnumber <= 12:
        
        # This is for special case for February (month 2), where we need to check for a leap year
        if monthnumber == 2:
            # This is to ask the user if the year is a leap year
            leap = input("Is it a leap year? (yes/no): ").strip().lower()
            # This is to check if it's a leap year, February will have 29 days; otherwise, it will have 28 days
            days = 29 if leap == "yes" else 28
        else:
            # This is for all other months, just look up the number of days in the dictionary
            days = days_of_months[monthnumber]
        
        # This is to output the number of days in the selected month
        print(f"The number of days in month {monthnumber} is {days}.")
    else:
        # This is to inform the user if the month number is invalid (not between 1 and 12)
        print("Oops! That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    # This is to handle cases where the user inputs something that isn't a number (e.g., text)
    print("Sorry, that's not a valid input. Please enter a number between 1 and 12.")