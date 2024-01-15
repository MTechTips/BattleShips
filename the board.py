from tkinter import *
import math
root = Tk()
board = []
buttons = []
global gamestate
for n in range (0,100):
    board.append(0)
def board_create():
    global gamestate
    x = 0
    y = 0
    n = 0
    for space in board:
        if space == 0:
            button = Button(root,text="     ", command=lambda n=n: shootandplace(n))     #under construction
            button.grid(row=y, column=x)
            buttons.append(button)
        else:
            label = Label(root, text=decode_symbol(space))
            label.grid(row=y,column=x)
            labels.append(label)
        x = x + 1
        if x>9:
            x = 0
            y = y + 2
        n = n + 1
        create_space = Label(root, text=" ")
        create_space.grid(row=19, column=0)
        game_state = Label(root, text=gamestate)
        game_state.place(x=0,y=260)
def state_change():
    global gamestate
    gamestate="change later"
def shootandplace(position):
    if placedships==false:
        place_ships(position)
    shoot(position)
board_create()