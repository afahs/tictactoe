from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")
char1='X'
char2='Y'
# Get char
char = input("Would you like to be \'X\' or \'O\'?")
if char == 'X':
    player2char='Y'
if char=='Y':
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
    n = int(input("Where would player one like to move?"))
    changechars()
    if not move(n, char):
        print("Invalid move!")
    if isWinnerX(board,char):
        print("X wins!")
    if isWinnerO(board,char):
        print("O wins!")
    input()
    
    
