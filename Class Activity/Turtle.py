import turtle

# Set up the drawing canvas
canvas = turtle.Screen()
canvas.bgcolor("beige")  # Set a beige background

# Prepare the turtle drawing
drawer = turtle.Turtle()
drawer.speed(20)  # Increase drawing speed

# Establish a recurring pattern
for count in range(150):  # Repeat 150 times
    drawer.forward(100)  # Move forward by 100 units
    drawer.left(50)      # Turn left by 50 degrees

# Wait for a click to close the canvas
canvas.exitonclick()
