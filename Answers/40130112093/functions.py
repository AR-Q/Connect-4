import numpy as np
import copy

def configure(x):
    return (x+1)*100

def configure_pos(x,y):

    # x = 4 - x
    # y = 4 - y

    return (configure(x), configure(y))

def configure_row(row):

    configured_row = copy.deepcopy(row)

    for i in range(5):

        if row[i] == 4:
            configured_row[i] = 500
        elif row[i] == 3:
            configured_row[i] = 400
        elif row[i] == 2:
            configured_row[i] = 300
        elif row[i] == 1:
            configured_row[i] = 200
        elif row[i] == 0:
            configured_row[i] = 100
    
    return configured_row

def get_bottom_row(board: np.array):

    row = [-1,-1,-1,-1,-1]

    for i in range(4, -1, -1):
        for j in range(5):

            if board[i][j] == 0 and row[j] == -1:
                row[j] = i

    return row



def endgame(board: np.array, turn):
    if v_win(board, turn):
        return turn
    elif h_win(board, turn):
        return turn
    elif d_win(board,turn):
        return turn
    elif draw(board):
        return 0
    
    return -1

        
def v_win(board: np.array, turn):
    
    for i in range(5):
        counter = 0
        for j in range(5):
            if board[j][i] == turn:
                counter += 1
            elif i != 4:
                counter = 0
        
        if counter >= 4:
            return True
    
    return False

def h_win(board: np.array, turn):

    for i in range(5):
        counter = 0
        for j in range(5):
            if board[i][j] == turn:
                counter += 1
            elif j != 4:
                counter = 0
        
        if counter >= 4:
            return True
    
    return False

def d_win(board: np.array, turn):
    
    try:
        for i in range(2):
            counter = 0
            for j in range(0,4):
                if board[j][j+i] == turn:
                    counter += 1
                else:
                    counter = 0
            
            if counter == 4:
                return True
    except:
        print("")
        
    try:
        for i in range(2):
            counter = 0
            for j in range(1,5):
                if board[j][j-i] == turn:
                    counter += 1
            
            if counter == 4:
                return True
    except:
        print("")
    
    try:

        for i in range(2):
            counter = 0
            for j in range(0,4):
                if board[j][3+i-j] == turn:
                    counter += 1
            
            if counter == 4:
                return True
    except:
        print("")
        
    try:

        for i in range(2):
            counter = 0
            for j in range(1,5):
                if board[j][4+i-j] == turn:
                    counter += 1
            
            if counter == 4:
                return True
    except:
        print("")
    
    return False



def draw(board: np.array):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                return False
            
    return True

a = np.array([
    [0,0,0,0,0],
    [1,0,0,0,0],
    [2,1,0,0,0],
    [1,1,1,0,0],
    [2,2,2,1,0]
])

print(d_win(a,1))
# print(get_bottom_row(a))