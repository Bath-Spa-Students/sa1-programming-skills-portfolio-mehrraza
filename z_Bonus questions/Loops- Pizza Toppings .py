print("Enter 'quit' when you are done adding your Pizza Toppings ")

#Will be using the while loop for the following code 
while True:
    #The following code will ask the user to input their favorite toppings
    pizza = input("Enter the Pizza Toppings as you prefer :")

    if pizza == 'quit':
        print("THANK YOU!, Now you are done adding toppings to your Pizza.")
        break #This will break the loop once the user types 'quit'.
    else:
        print(f"I will add that {pizza} topping to your pizza")