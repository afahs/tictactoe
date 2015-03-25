from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")

# Get char
char = input("Would player two like to be \'X\' or \'O\'?")
if char == 'X':
    player2char='O'
if char=='O':
    player2char='X'
# TODO: Check if char is 'X' or 'O'

# Check whether or not to display instructions
a = input("Do you want instructions?").upper()
if a.startswith("Y"):
    drawInstructionBoard()

# Initialize and draw board
initBoard()

def changechars():
    global char
    if char == "X":
        char = "O"
    elif char == "O":
        char = "X"

# Start the game
while True:
    drawBoard()
    changechars()
    n = int(input("Where would " + char + "like to move?"))
    if not move(n, char):
        print("Invalid move!")
    if isWinnerX(board,char):
        print("X wins!")
    if isWinnerO(board,char):
        print("O wins!")
    
    
    
