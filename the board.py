from tkinter import *
import math
root = Tk()
board = []
buttons = []
for n in range (0,100):
    board.append(0)
def board_create():
    x = 0
    y = 0
    n = 0
    for space in board:
        if space == 0:
            button = Button(root,text="     ", command=lambda n=n: shoot(n))
            button.grid(row=y, column=x)
            buttons.append(button)
        else:
            label = Label(root, text=decode_symbol(space))
            label.grid(row=y, column=x)
            labels.append(label)
        x = x + 1
        if x>9:
            x = 0
            y = y + 2
        n = n + 1
def shoot(position):
    print(position)
board_create()