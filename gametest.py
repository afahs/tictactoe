from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")

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

# Start the game
while True:
    drawBoard()
    n = int(input("Where would player one like to move?"))
    if not move(n, char):
        print("Invalid move!")
    if isWinner(board,char):
        print("You win!")
    n2 = int(input("Where would player two like to move?"))
    input()
    
    
