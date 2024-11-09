from turtle import *

penup()
setpos(-225, 225)
pendown()
printed = []
key = {0: (-150, 150), 1: (0, 150), 2: (150, 150), 3: (-150, 0), 4: (0, 0), 5: (150, 0), 6: (-150, -150), 7: (0, -150),
       8: (150, -150)}


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

def draw_board():
    pensize(2.5)
    tracer(0)
    hideturtle()
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
    tracer(1)
    speed(0.5)


def draw_O(coord):

    x, y = coord
    pensize(5)
    penup()
    setpos(x, y - 55)
    pendown()
    circle(55)
    # penup()


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
    # penup()






if __name__ == "__main__":
    speed(0)
    draw_board()
    setpos(-225, 225)





    hideturtle()
    penup()
    # 0
    setpos(key[0])
    pendown()
    dot(5)
    penup()

    # 1
    setpos(key[1])
    pendown()
    dot(5)
    penup()
    # 2
    setpos( key[2])
    pendown()
    dot(5)
    penup()

    # 3
    setpos(key[3])
    pendown()
    dot(5)
    penup()

    # 4
    setpos(key[4])
    pendown()
    dot(5)
    penup()

    # 5
    setpos(key[5])
    pendown()
    dot(5)
    penup()

    # 6
    setpos(key[6])
    pendown()
    dot(5)
    penup()

    # 7
    setpos(key[7])
    pendown()
    dot(5)
    penup()

    # 8
    setpos(key[7])
    pendown()
    dot(5)


    draw_X(key[0])
    draw_O(key[1])
    draw_X(key[2])
    draw_O(key[8])


    setpos(key[0])

    done()