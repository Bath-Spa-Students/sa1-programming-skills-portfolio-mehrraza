# Dictionary to store the number of days in each month
# Declaring the variable days_of_months.
days_of_months = {
    1: 31,   # January
    2: 28,   # February (assuming a non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# This is to ask the user to input a month number, with a gentle prompt
try:
    monthnumber = int(input("Please enter a month number (1-12): ").strip()) # .strip() Removes extra spaces around input

    # This is to check if the month number is within the valid range
    if monthnumber in days_of_months:
        # This is to print the number of days for the entered month
        print(f"The number of days in month {monthnumber} is {days_of_months[monthnumber]}.")
    else:
        # This is to inform the user if the input is outside the range of 1-12
        print("Oops! That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    # This is to handle non-integer input gracefully with a friendly message
    print("Invalid input. Please enter a numerical value between 1 and 12.")