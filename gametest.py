from boardfunc import *

# Print welcome message
print("Welcome to TicTacToe!")
# Get char
char = input("Would you like to be \'X\' or \'O\'?")
# Check if char is 'X' or 'O'


a=input("Do you want instructions?")
if a=="YES":
    drawinstructionBoard()
 
if a=="NO":
    initBoard()
    drawBoard()
input()
