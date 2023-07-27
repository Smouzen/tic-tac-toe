import random as rn

board = ["-","-","-"
         ,"-","-","-"
         ,"-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True

##creating for pllayers
def createBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
   # print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    #print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

##take user unput

def playInput(board):
    print("current player"+currentPlayer)
    userInput  = int(input("Enter a number from 1-9\n"))
    if userInput>=1 and userInput <=9 and  board[userInput-1] == "-":
        board[userInput-1] = currentPlayer
    else:
        print("Try a different spot")

##check for the winner per row
def checkResultsRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

##check for the winner per column
def checkResultsColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

##check for the winner per column
def checkResultsDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[1]
        return True
    
#check the winner
def checkWinner():
    if checkResultsRow(board) or checkResultsColumn(board) or checkResultsDiagonal(board):
        print(f" The winer is{winner}")

##check if its draw
def checkDraw(board):
    global gameRunning
    if "-" not in board:
        createBoard(board)
        print("It is a tie")
        gameRunning = False


def switchPlayers():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "0":
        position = rn.randint(0, 8)
        if board[position]== "-":
            board[position] = "0"
            switchPlayers()


while gameRunning:
    createBoard(board)
    playInput(board)
    checkWinner()
    checkDraw(board)
    switchPlayers()
    computer(board)
    checkWinner()
    checkDraw(board)
