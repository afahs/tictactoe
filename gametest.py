from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")

# Get char
char = input("Would you like to be \'X\' or \'O\'?")
if char == 'X':
    compchar='Y'
if char=='Y':
    compchar='X'
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
    n = int(input("Where would you like to move?"))
    if n!=11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39:
        print("invalid move!")
    if not move(n, char):
        print("Invalid move!")
    if isWinner(board,char):
        print("You win!")
    input()
    
