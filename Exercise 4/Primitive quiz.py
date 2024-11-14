# This is to ask the user to name the capital of France, ignoring any extra spaces
useranswer = input("Can you name the capital of France? ").strip() # .strip() Removes extra spaces around input

# This is to check if the answer is correct, ignoring case differences
if useranswer.lower() == "paris":
    # This is to let the user know they got it right
    print("That's right! The capital of France is Paris.")
else:
    # This is for gently let the user know the answer is incorrect
    print("Oops, not quite! The correct answer is Paris.")

