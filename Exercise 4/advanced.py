# A dictionary structure allows you to easily retrieve the capital for a given country to a quiz
#These are the names of  country names, and the values are their capitals
country_names = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Switzerland": "Bern",
    "Greece": "Athens"
}

# This is the variable to keep track of the user's score
score = 0

# This is the loop through each country-capital pair in the quiz
for country, capital in country_names.items():
    # This is to ask the user for the capital of the current country
    useranswer = input(f"What's the capital of {country}? ").strip() # .strip() Removes extra spaces around input

    # This is to check if the answer is correct, ignoring case differences
    if useranswer.lower() == capital.lower():
        # This is to if appropriate, acknowledge and add to the score
        print("Nice! That's correct.")
        score += 1
    else:
        # This is to check if appropriate, gently provide the correct answer
        print(f"Close, but the capital of {country} is actually {capital}.")

# This is to display the user's final score with encouragement
print(f"\nGreat job! You scored {score} out of {len(country_names)}.")
