from tkinter import *
import math
root = Tk()
board = []
buttons = []
global gamestate
click = False
placedships = False
for n in range (0,100):
    board.append(0)
def board_create():
    global gamestate
    x = 0
    y = 0
    n = 0
    for space in board:
        if space == 0:
            button = Button(root,text="     ", command=lambda n=n: shootandplace(n))
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
        game_state = Label(root, text=state_change())
        game_state.place(x=0,y=260)
def state_change():
    gamestate="change later"
    return gamestate
def shootandplace(position):
    if placedships==False:
        place_ships(position)
    if placedships==True:
        makearray(position)
def place_ships(pos):
    global click
    
def shoot(pos):
    pass
def mode():
    pass
def datacollect():
    global mode
    global click
    global position
    onbuttonpress(mode,click,position)
def onbuttonpress():
    pass
board_create()