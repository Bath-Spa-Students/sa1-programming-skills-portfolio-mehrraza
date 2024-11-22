# Two primary categories of functions exist:
#1. Void functions Don't return a value after performing an action.

#2. Functions with value returns: These functions process input before returning a value.


# Function names (such as `find_max` and `compute_sum`) should make it obvious what they are used for.
### A function can be defined using the `def` keyword.

# It's important to indent within a function body.


# A void function illustration
def display_message():
    print("This is a void function!")

# Making use of the void function
display_message()

# Local variable example
def display_message():
    hehe = "This is a local variable example!"  # `text` is only accessible within this function.
    print(hehe)

display_message()

# Uncommenting the next line will raise a NameError:
# print(hehe)
# Functions that have the same local variable names don't conflict with one another.

def func3():
    data = "Local to func3"
    print(data)

def func2():
    info = "Local to func2"
    print(info)

func3()
func2()

# Passing arguments to a function
def say_hello(welcome):  # `welcome` is a parameter.
    print(welcome)

letter = "Good Afternoon"
say_hello(letter)  # Using the argument `letter`.

# Function to determine a given number's double
def main():
    number = 3
    calculate_double(number)

def calculate_double(worth):
    print(worth * 2)

main()

# A function example with several arguments
def student_info(name, marks):
    print(f"Student Name: {name}, Grade: {marks}")

student_info("RaZa", "B+")


