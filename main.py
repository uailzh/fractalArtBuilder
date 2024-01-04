from turtle import *

# Function to draw a tree using recursion
def tree(size, levels, angle):
    # Base case: if no more levels, draw a green dot
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    # Draw the trunk of the tree
    forward(size)
    right(angle)

    # Recursively draw the left subtree
    tree(size * 0.8, levels - 1, angle)

    # Move to the right subtree position
    left(angle * 2)
    # Recursively draw the right subtree
    tree(size * 0.8, levels - 1, angle)
    # Move back to the original position
    right(angle)
    # Move back to the base of the trunk
    backward(size)

# Function to draw one side of a snowflake
def snowflake_side(length, levels):
    # Base case: if no more levels, draw a line
    if levels == 0:
        forward(length)
        return

    # Divide the length by 3 to create segments
    length /= 3.0
    # Recursively draw the left segment
    snowflake_side(length, levels - 1)
    # Turn left 60 degrees for the next segment
    left(60)
    # Recursively draw the center segment
    snowflake_side(length, levels - 1)
    # Turn right 120 degrees for the next segment
    right(120)
    # Recursively draw the right segment
    snowflake_side(length, levels - 1)
    # Turn left 60 degrees for the next segment
    left(60)
    # Recursively draw the last center segment
    snowflake_side(length, levels - 1)

# Function to create a snowflake with a specified number of sides
def create_snowflake(sides, length):
    # List of colors for each side of the snowflake
    colors = ["blue", "green", "red", "black"]
    for i in range(sides):
        # Set the color for the current side
        color(colors[i])
        # Draw one side of the snowflake
        snowflake_side(length, sides)
        # Turn right to prepare for the next side
        right(360/sides)

# Draw a snowflake with 3 sides and length 200
create_snowflake(3, 200)

# Turn the turtle to draw the tree
left(90)
# Draw a tree with size 70, 7 levels, and angle 30 degrees
tree(70, 7, 30)

# Keep the turtle graphics window open until closed
mainloop()
