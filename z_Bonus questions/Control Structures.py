# The following code will check the alien's color and print the output accordingly.
alien_color = input("Enter the color of the alien : ").strip().lower()

if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("No points earned this time!")