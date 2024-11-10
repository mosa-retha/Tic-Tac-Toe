from turtle import *
import tkinter as tk

# Stores previously drawn elements, for easier reference
printed = []

# Maps grid position (0-8) to screen coordinates
key = {0: (-150, 150), 1: (0, 150), 2: (150, 150), 3: (-150, 0), 4: (0, 0),
       5: (150, 0), 6: (-150, -150), 7: (0, -150), 8: (150, -150)}

# Function to set up the turtle graphics window properties
def set_window_properties():
    root = Screen()._root
    root.attributes("-topmost", True)  # Make the window stay on top of other windows
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button
    root.update()

# Function to prompt the user to choose between CPU and Player as an opponent
def get_user_player_type():
    def player():
        # Set variable to "player" and close the prompt window
        play_var.set("player")
        root.quit()
        root.destroy()

    def cpu():
        # Set variable to "cpu" and close the prompt window
        play_var.set("cpu")
        root.quit()
        root.destroy()

    # Create the Tkinter window for the prompt
    root = tk.Tk()
    root.title("User Input Prompt")

    # Add label and buttons for choosing opponent type
    tk.Label(root, text="Do you want to play with CPU or Player?").pack()
    play_var = tk.StringVar()

    # Buttons for "Player" and "CPU" options
    tk.Button(root, text="Player", command=player).pack()
    tk.Button(root, text="CPU", command=cpu).pack()

    # Start the Tkinter main loop and wait for user input
    root.mainloop()
    return play_var.get().lower()

# Function to draw an individual square, with an optional fill
def draw_square(size=150, fill=False):
    if fill:
        pencolor("white")  # Set pen color to white to erase existing content
        fillcolor("white")  # Fill color is also set to white
        begin_fill()
    for i in range(4):  # Draw a square by moving forward and turning right
        forward(size)
        right(90)
    if fill:
        end_fill()  # End the filling if fill was enabled
        pencolor("black")  # Reset the pen color to black

# Function to erase a line by drawing over it with a thick white line
def erase_line(x1, y1, x2, y2):
    penup()
    setpos(x1, y1)
    pendown()
    color("white")  # Set color to white for erasing
    width(5)  # Set line width to cover original line width
    setpos(x2, y2)  # Draw line from (x1, y1) to (x2, y2)
    color("black")  # Reset color to black
    width(1)  # Reset width to original value

# Function to draw or erase a number at a specific grid coordinate
def draw_number(number, coord, erase=False):
    x, y = coord
    penup()
    setpos(x - 20, y - 40)  # Adjust position to center the number in the square
    pendown()
    if erase:
        # If erase is True, fill the square with white to "erase" the number
        penup()
        setpos(x - 20, y + 40)  # Move to upper-left corner of square
        pendown()
        draw_square(80, fill=True)  # Fill the square with background color
    else:
        # Draw the number in a light gray color to show position indicators
        pencolor("lightgray")
        write(number, font=("Arial", 48, "normal"))
        pencolor("black")  # Reset pen color to black

# Function to draw the Tic-Tac-Toe board layout
def draw_board():
    hideturtle()  # Hide the turtle cursor for clean drawing
    pensize(2.5)  # Set pen size for thicker grid lines
    penup()
    setpos(-225, 225)  # Move to starting position for top-left square
    pendown()
    tracer(0)  # Disable automatic screen updates for faster drawing
    speed(0)  # Max speed for faster drawing

    # Draw a 3x3 grid of squares
    for i in range(3):
        for j in range(3):
            draw_square()  # Draw each square in the grid
            forward(150)  # Move to next square position in the row
        backward(450)  # Move back to the left side of the grid
        right(90)
        forward(150)  # Move down to the next row
        left(90)

    # Erase the outer grid lines for a cleaner appearance
    erase_line(-225, 225, 225, 225)  # Top border
    erase_line(225, 225, 225, -225)  # Right border
    erase_line(225, -225, -225, -225)  # Bottom border
    erase_line(-225, -225, -225, 225)  # Left border

    # Display grid numbers to show square positions (1-9)
    k = [i for i in range(1, 10)]
    for i in range(3):
        # Draw numbers in the corresponding grid squares
        draw_number(k[:5:-1][i], key[i])  # Top row
        draw_number(k[3:6:][i], key[i + 3])  # Middle row
        draw_number(k[:3][i], key[i + 6])  # Bottom row

    tracer(1)  # Enable screen updates again
    speed(0.5)  # Set speed to a moderate level

# Function to draw an "O" symbol at the specified grid coordinate
def draw_O(coord):
    x, y = coord
    pensize(5)  # Set pen size for drawing "O"
    penup()
    setpos(x, y - 55)  # Move to starting position slightly below center
    pendown()
    circle(55)  # Draw a circle with radius 55 for "O"

# Function to draw an "X" symbol at the specified grid coordinate
def draw_X(coord):
    x, y = coord
    pensize(5)  # Set pen size for drawing "X"
    penup()
    setpos(x - 50, y + 50)  # Move to top-left corner of the "X"
    pendown()
    setpos(x + 50, y - 50)  # Draw diagonal line to bottom-right
    penup()
    setpos(x + 50, y + 50)  # Move to top-right corner
    pendown()
    setpos(x - 50, y - 50)  # Draw diagonal line to bottom-left

# Main program execution
if __name__ == "__main__":
    set_window_properties()  # Set up turtle window properties
    play_view = get_user_player_type()  # Get user choice of "Player" or "CPU"
    done()  # Close the turtle graphics session when done
