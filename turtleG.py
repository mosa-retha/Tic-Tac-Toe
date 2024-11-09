from turtle import *

import tkinter as tk

printed = []
key = {0: (-150, 150), 1: (0, 150), 2: (150, 150), 3: (-150, 0), 4: (0, 0), 5: (150, 0), 6: (-150, -150), 7: (0, -150),
       8: (150, -150)}


def set_window_properties():
    root = Screen()._root
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button
    root.update()


def get_user_player_type():
    def player():
        play_var.set("player")
        root.quit()
        root.destroy()

    def cpu():
        play_var.set("cpu")
        root.quit()
        root.destroy()

    root = tk.Tk()
    root.title("User Input Prompt")

    tk.Label(root, text="Do you want to play with CPU or Player?").pack()

    play_var = tk.StringVar()

    tk.Button(root, text="Player", command=player).pack()
    tk.Button(root, text="CPU", command=cpu).pack()

    root.mainloop()
    return play_var.get().lower()

def draw_square():
    for i in range(4):
        forward(150)
        right(90)


def erase_line(x1, y1, x2, y2):
    penup()
    setpos(x1, y1)
    pendown()
    color("white")  # Assuming the background is white
    width(5)  # Set the width to be slightly larger than the original line
    setpos(x2, y2)
    color("black")  # Reset the color to black
    width(1)  # Reset the width to the original value


def draw_number(number, coord, erase=False):
    x, y = coord
    penup()
    setpos(x - 20, y - 40)  # Adjust position to center the number
    pendown()
    if erase:
        pencolor("white")  # Use the background color to erase
    else:
        pencolor("lightgray")  # Use a light color to simulate translucency
    write(number, font=("Arial", 48, "normal"))
    pencolor("black")  # Reset the color to black


def draw_board():
    hideturtle()
    pensize(2.5)
    penup()
    setpos(-225, 225)
    pendown()
    tracer(0)
    speed(0)
    for i in range(3):
        for j in range(3):
            draw_square()
            forward(150)
        backward(450)
        right(90)
        forward(150)
        left(90)
    erase_line(-225, 225, 225, 225)
    erase_line(225, 225, 225, -225)
    erase_line(225, -225, -225, -225)
    erase_line(-225, -225, -225, 225)

    k = [ i for i in range(1, 10)]

    for i in range(3):
        draw_number(k[:5:-1][i], key[i])
        draw_number(k[3:6:][i], key[i+3])
        draw_number(k[:3][i], key[i+6])

    tracer(1)
    speed(0.5)


def draw_O(coord):

    x, y = coord
    pensize(5)
    penup()
    setpos(x, y - 55)
    pendown()
    circle(55)



def draw_X(coord):
    x, y = coord
    pensize(5)
    penup()
    setpos(x - 50, y + 50)
    pendown()
    setpos(x + 50, y - 50)
    penup()
    setpos(x + 50, y + 50)
    pendown()
    setpos(x - 50, y - 50)



if __name__ == "__main__":
    set_window_properties()
    play_view = get_user_player_type()
    done()