from boardfunc import *
import random
# Print welcome message
print("Welcome to TicTacToe!")

# Get char
char = input("Would player two like to be \'X\' or \'O\'?").upper()
if not (char=='X' or char=='O'):
    print("Invalid choice, your character will be selected randomly")
    if random.randint(1,2)==1:
        char='X'
    else:
        char='O'
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
    n = input("Where would " + char + " like to move?")
    if n=="":
         print("Invlaid move, your position will be selected randomly")
         n=str(random.randint(11,39))
    if not(n.startswith('1') or (n.startswith('2')) or (n.startswith('3'))):
           print("Invlaid move, your position will be selected randomly")
           n=str(random.randint(11,39))  
    n=int(n)
    if not (n>10 and n<40):
         print("Invlaid move, your position will be selected randomly")
         n=random.randint(11,39)
    if not move(n, char):
        print("Invalid move!")
    if isWinnerX(board,char):
        print("X wins!")
    if isWinnerO(board,char):
        print("O wins!")
    
    
    
