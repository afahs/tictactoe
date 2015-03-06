from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")

# Get char
char = input("Would you like to be \'X\' or \'O\'?")

# TODO: Check if char is 'X' or 'O'

# Check whether or not to display instructions
a = input("Do you want instructions?").upper()
if a.startswith("Y"):
    drawinstructionBoard()

# Initialize and draw board
initBoard()
drawBoard()
