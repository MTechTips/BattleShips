#ask sir how to reset the text file every time the program is run and how everyone else can work with the text files because they are in my one drive
turn = 1
position = "A3"
def make_guess(turn,position):
    if turn == 1:
        board2 = open("board2.txt","a")
        board2.write(position)
        
        

def shoot():
    pass


make_guess(turn, position)