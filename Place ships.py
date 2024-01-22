#Ships needed:
#1x5
#1x4
#2x3
#1x2
mode = "place"
click = False
position = 99

def makearray(position): #called from when need to shoot.
    occupied = [[],[],[],[],[]]
    shoot(occupied)

def onbuttonpress(mode,click,position):
    if mode == "place":
        valid_move_check(click,position)
    if mode == "attack":
        makearray(position)

def valid_move_check(click,position):
    #makeboard()
    valid_move = True
    placed = False
    #click is the 1 or 2 to denote if it's first or second time clicked
    row = str(position)[0:1]
    column = str(position)[1:2]
    print(row)
    print(column)

    ship5 = 1 #ship5[0] = count of how many of that type left, ship5[1] = length of ship
    ship4 = 1
    ship3 = 2
    ship2 = 1
    
    hori_possible_area = []
    vert_possible_area = []
    
    if click == False: #1st click
        start_pos = position
        '''for n in range [2,6]:
            if ship+str(n)[0] > 0:'''
        #check if there are any ships left to place
        
        if ship2 > 0:
            horia1 = position+1 #ALL OF THESE ARE NOT RIGHT
            horim1 = position-1 
            if str(horia1)[0:1] == str(position)[0:1] and horia1<99:#if the space is not in the same row as the original position, dont add it to the list
                hori_possible_area.append(horia1)
            if str(horim1)[0:1] == str(position)[0:1] and horim1>0:
                hori_possible_area.append(horim1)
            else:
                print("Not in same row or off board")
            
            verta1 = position+10 #ALL OF THESE ARE NOT RIGHT
            vertm1 = position-10 
            if str(verta1)[1:2] == str(position)[1:2] and verta1<99:
                vert_possible_area.append(verta1)
            if str(vertm1)[1:2] == str(position)[1:2] and vertm1>0:
                vert_possible_area.append(vertm1)
            else:
                print("Not in same row or off board")
        if ship3 > 0:
            horia2 = position+2
            horim2 = position-2
            if str(horia2)[0:1] == str(position)[0:1] and horia2<99:    
                hori_possible_area.append(horia2)
            if str(horim2)[0:1] == str(position)[0:1] and horim2>0:
                hori_possible_area.append(horim2)
            else:
                print("Not in same row or off board")
                
            verta2 = position+10 #ALL OF THESE ARE NOT RIGHT
            vertm2 = position-10 
            if str(verta2)[1:2] == str(position)[1:2] and verta2<99:
                vert_possible_area.append(verta2)
            if str(vertm2)[1:2] == str(position)[1:2] and vertm2>0:
                vert_possible_area.append(vertm2)
            else:
                print("Not in same row or off board")

        if ship4 > 0:
            horia3 = position+3
            horim3 = position-3
            if str(horia3)[0:1] == str(position)[0:1] and horia3<99:
                vert_possible_area.append(horia3)
            if str(horim3)[0:1] == str(position)[0:1] and horim3>0:
                vert_possible_area.append(horim3)
            else:
                print("Not in same row or off board")
                
            verta3 = position+10 #ALL OF THESE ARE NOT RIGHT
            vertm3 = position-10 
            if str(verta3)[1:2] == str(position)[1:2] and verta3<99:
                vert_possible_area.append(verta3)
            if str(vertm3)[1:2] == str(position)[1:2] and vertm3>0:
                vert_possible_area.append(vertm3)
            else:
                print("Not in same row or off board")
            
        if ship5 > 0:
            horia4 = position+4
            horim4 = position-4
            if str(horia4)[0:1] == str(position)[0:1] and horia4<99:
                hori_possible_area.append(horia4)
            if str(horim4)[0:1] == str(position)[0:1] and horim4>0:
                hori_possible_area.append(horim4)
            else:
                print("Not in same row")
                
            verta4 = position+10 #ALL OF THESE ARE NOT RIGHT
            vertm4 = position-10 
            if str(verta4)[1:2] == str(position)[1:2] and verta4<99:
                vert_possible_area.append(verta4)
            if str(vertm4)[1:2] == str(position)[1:2] and vertm4>0:
                vert_possible_area.append(vertm4)
            else:
                print("Not in same row or off board")
            print(hori_possible_area)
            print(vert_possible_area)
        else:
            placed = True

    elif click == True: #2nd click
        end_pos = position
        if end_pos not in hori_possible_area and end_pos not in vert_possible_area:
            valid_move = False
            impossible_place_msg = "Cannot place ship there"
            return impossible_place_msg
    else:
        print("Something is wrong with the 'click' variable")
    
    
    

    return placed
    return start_pos
    return end_pos

#start_pos = start_pos
#end_pos = end_pos
def place_ships(start_pos, end_pos):
    pass
    
    
    
    
    
onbuttonpress(mode,click,position)