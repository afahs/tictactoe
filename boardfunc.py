# Initialize board
board = list(range(0, 40));
    
# Clear board
def initBoard():
    for i in range(0, 40):
        board[i] = ' '

# Display instructions
def drawInstructionBoard():
    board = list(range(0, 40));
    print('    |    |')
    print(' ' + str(board[17]) + ' | ' + str(board[18]) + ' | ' + str(board[19]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[14]) + ' | ' + str(board[15]) + ' | ' + str(board[16]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[11]) + ' | ' + str(board[12]) + ' | ' + str(board[13]))
    print('    |    |')
    print(' ')
    print('    |    |')
    print(' ' + str(board[27]) + ' | ' + str(board[28]) + ' | ' + str(board[29]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[24]) + ' | ' + str(board[25]) + ' | ' + str(board[26]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[21]) + ' | ' + str(board[22]) + ' | ' + str(board[23]))
    print('    |    |')
    print(' ')
    print('    |    |')
    print(' ' + str(board[37]) + ' | ' + str(board[38]) + ' | ' + str(board[39]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[34]) + ' | ' + str(board[35]) + ' | ' + str(board[36]))
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[31]) + ' | ' + str(board[32]) + ' | ' + str(board[33]))
    print('    |    |')

# Display board
def drawBoard():
    print('   |   |')
    print(' ' + str(board[17]) + ' | ' + str(board[18]) + ' | ' + str(board[19]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[14]) + ' | ' + str(board[15]) + ' | ' + str(board[16]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[11]) + ' | ' + str(board[12]) + ' | ' + str(board[13]))
    print('   |   |')
    print(' ')
    print('   |   |')
    print(' ' + str(board[27]) + ' | ' + str(board[28]) + ' | ' + str(board[29]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[24]) + ' | ' + str(board[25]) + ' | ' + str(board[26]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[21]) + ' | ' + str(board[22]) + ' | ' + str(board[23]))
    print('   |   |')
    print(' ')
    print('   |   |')
    print(' ' + str(board[37]) + ' | ' + str(board[38]) + ' | ' + str(board[39]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[34]) + ' | ' + str(board[35]) + ' | ' + str(board[36]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[31] + ' | ' + board[32] + ' | ' + board[33])
    print('   |   |')

# Make given move
def move(n, c):
    if (board[n] == ' '):
        board[n] = c
        return True
    return False
#win conditions


def isWinnerX(board,char):
    char1='X'
    return((board[17]==char1 and board[18]==char1 and board[19]==char1) or
           (board[14]==char1 and board[15]==char1 and board[16]==char1) or
           (board[11]==char1 and board[12]==char1 and board[13]==char1) or
           (board[17]==char1 and board[15]==char1 and board[13]==char1) or
           (board[19]==char1 and board[15]==char1 and board[11]==char1) or
           (board[17]==char1 and board[14]==char1 and board[11]==char1) or
           (board[18]==char1 and board[15]==char1 and board[12]==char1) or
           (board[19]==char1 and board[16]==char1 and board[13]==char1) or
#first board
           (board[27]==char1 and board[28]==char1 and board[29]==char1) or
           (board[24]==char1 and board[25]==char1 and board[26]==char1) or
           (board[21]==char1 and board[22]==char1 and board[23]==char1) or
           (board[27]==char1 and board[25]==char1 and board[23]==char1) or
           (board[29]==char1 and board[25]==char1 and board[21]==char1) or
           (board[27]==char1 and board[24]==char1 and board[21]==char1) or
           (board[28]==char1 and board[25]==char1 and board[22]==char1) or
           (board[29]==char1 and board[26]==char1 and board[23]==char1) or
#second board
           (board[37]==char1 and board[38]==char1 and board[39]==char1) or
           (board[34]==char1 and board[35]==char1 and board[36]==char1) or
           (board[31]==char1 and board[32]==char1 and board[33]==char1) or
           (board[37]==char1 and board[35]==char1 and board[33]==char1) or
           (board[39]==char1 and board[35]==char1 and board[31]==char1) or
           (board[37]==char1 and board[34]==char1 and board[31]==char1) or
           (board[38]==char1 and board[35]==char1 and board[32]==char1) or
           (board[39]==char1 and board[36]==char1 and board[33]==char1) or
#third board
           (board[17]==char1 and board[27]==char1 and board[37]==char1) or
           (board[18]==char1 and board[28]==char1 and board[38]==char1) or
           (board[19]==char1 and board[29]==char1 and board[39]==char1) or
           (board[14]==char1 and board[24]==char1 and board[34]==char1) or
           (board[15]==char1 and board[25]==char1 and board[35]==char1) or
           (board[16]==char1 and board[26]==char1 and board[36]==char1) or
           (board[11]==char1 and board[21]==char1 and board[31]==char1) or
           (board[12]==char1 and board[22]==char1 and board[32]==char1) or
           (board[13]==char1 and board[23]==char1 and board[33]==char1) or
           (board[17]==char1 and board[25]==char1 and board[33]==char1) or
           (board[11]==char1 and board[25]==char1 and board[39]==char1) or
           (board[13]==char1 and board[25]==char1 and board[37]==char1) or
           (board[19]==char1 and board[25]==char1 and board[31]==char1))
#cross board conditions

def isWinnerO(board,char):
    char2='O'
    return((board[17]==char2 and board[18]==char2 and board[19]==char2) or
           (board[14]==char2 and board[15]==char2 and board[16]==char2) or
           (board[11]==char2 and board[12]==char2 and board[13]==char2) or
           (board[17]==char2 and board[15]==char2 and board[13]==char2) or
           (board[19]==char2 and board[15]==char2 and board[11]==char2) or
           (board[17]==char2 and board[14]==char2 and board[11]==char2) or
           (board[18]==char2 and board[15]==char2 and board[12]==char2) or
           (board[19]==char2 and board[16]==char2 and board[13]==char2) or
#first board
           (board[27]==char2 and board[28]==char2 and board[29]==char2) or
           (board[24]==char2 and board[25]==char2 and board[26]==char2) or
           (board[21]==char2 and board[22]==char2 and board[23]==char2) or
           (board[27]==char2 and board[25]==char2 and board[23]==char2) or
           (board[29]==char2 and board[25]==char2 and board[21]==char2) or
           (board[27]==char2 and board[24]==char2 and board[21]==char2) or
           (board[28]==char2 and board[25]==char2 and board[22]==char2) or
           (board[29]==char2 and board[26]==char2 and board[23]==char2) or
#second board
           (board[37]==char2 and board[38]==char2 and board[39]==char2) or
           (board[34]==char2 and board[35]==char2 and board[36]==char2) or
           (board[31]==char2 and board[32]==char2 and board[33]==char2) or
           (board[37]==char2 and board[35]==char2 and board[33]==char2) or
           (board[39]==char2 and board[35]==char2 and board[31]==char2) or
           (board[37]==char2 and board[34]==char2 and board[31]==char2) or
           (board[38]==char2 and board[35]==char2 and board[32]==char2) or
           (board[39]==char2 and board[36]==char2 and board[33]==char2) or
#third board
           (board[17]==char2 and board[27]==char2 and board[37]==char2) or
           (board[18]==char2 and board[28]==char2 and board[38]==char2) or
           (board[19]==char2 and board[29]==char2 and board[39]==char2) or
           (board[14]==char2 and board[24]==char2 and board[34]==char2) or
           (board[15]==char2 and board[25]==char2 and board[35]==char2) or
           (board[16]==char2 and board[26]==char2 and board[36]==char2) or
           (board[11]==char2 and board[21]==char2 and board[31]==char2) or
           (board[12]==char2 and board[22]==char2 and board[32]==char2) or
           (board[13]==char2 and board[23]==char2 and board[33]==char2) or
           (board[17]==char2 and board[25]==char2 and board[33]==char2) or
           (board[11]==char2 and board[25]==char2 and board[39]==char2) or
           (board[13]==char2 and board[25]==char2 and board[37]==char2) or
           (board[19]==char2 and board[25]==char2 and board[31]==char2))
#cross board conditions
 
    
    
