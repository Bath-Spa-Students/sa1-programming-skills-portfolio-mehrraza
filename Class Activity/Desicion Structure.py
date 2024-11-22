# Request sales information from the user
profit = int(input("Enter profit: "))

# Initialize bonus variable
extra = 0

# Verify the state of profit.
if profit > 50000:
    extra = 500  # Assign bonus if condition is met
else:
    extra = 0  # No bonus for profit <= 50000

# Show the bonus that was calculated.
print("Your Extra Pay is " + str(extra))

