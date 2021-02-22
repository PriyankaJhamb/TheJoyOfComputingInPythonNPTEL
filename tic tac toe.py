#tic tac toe game
import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s='X'
p2s='O'
def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
                print(symbol,"won")
                return True
    return False
                
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
    return False
            

def check_diagonal(symbol):
    if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
        print(symbol,"won")
        return True
    if board[1][1]==symbol and board[1][1]==symbol and board[2][2]==symbol:
        print(symbol,"won")
        return True
    '''
    # another method
    c=0
    for i in range(3):
        if board[i][i]==symbol :
            c=c+1
    if c==3:
        print(symbol,"won")
        return True
    
    d=0
    for j in range(3):
        if board[0+j][2-j]==symbol:
            d=d+1
    if d==3:
        print(symbol,"won")
        return True
    '''
    return False

def won(p):
    return check_row(p) or check_col(p) or check_diagonal(p)
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row number  1 or 2 or 3:"))
        column=int(input('Enter column number 1 or 2 or 3:'))
        if row>0 and row<4 and column<4 and column>0 and board[row-1][column-1]=='_' :
            
            break
        else:
            print("Invalid. Enter row and coulmn number again. ")
    board[row-1][column-1]=symbol



def play():
    for turn in range(9):
        if(turn%2==0):
            print("X turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not (won(p2s)):
        print("Draw. Try again")   
    
play()