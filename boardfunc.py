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
def isWinner(board,char):
    return((board[17]==char and board[18]==char and board[19]==char) or
           (board[14]==char and board[15]==char and board[16]==char) or
           (board[11]==char and board[12]==char and board[13]==char) or
           (board[17]==char and board[15]==char and board[13]==char) or
           (board[19]==char and board[15]==char and board[11]==char) or
           (board[17]==char and board[14]==char and board[11]==char) or
           (board[18]==char and board[15]==char and board[12]==char) or
           (board[19]==char and board[16]==char and board[13]==char) or
#first board
           (board[27]==char and board[28]==char and board[29]==char) or
           (board[24]==char and board[25]==char and board[26]==char) or
           (board[21]==char and board[22]==char and board[23]==char) or
           (board[27]==char and board[25]==char and board[23]==char) or
           (board[29]==char and board[25]==char and board[21]==char) or
           (board[27]==char and board[24]==char and board[21]==char) or
           (board[28]==char and board[25]==char and board[22]==char) or
           (board[29]==char and board[26]==char and board[23]==char) or
#second board
           (board[37]==char and board[38]==char and board[39]==char) or
           (board[34]==char and board[35]==char and board[36]==char) or
           (board[31]==char and board[32]==char and board[33]==char) or
           (board[37]==char and board[35]==char and board[33]==char) or
           (board[39]==char and board[35]==char and board[31]==char) or
           (board[37]==char and board[34]==char and board[31]==char) or
           (board[38]==char and board[35]==char and board[32]==char) or
           (board[39]==char and board[36]==char and board[33]==char) or
#third board
           (board[17]==char and board[27]==char and board[37]==char) or
           (board[18]==char and board[28]==char and board[38]==char) or
           (board[19]==char and board[29]==char and board[39]==char) or
           (board[14]==char and board[24]==char and board[34]==char) or
           (board[15]==char and board[25]==char and board[35]==char) or
           (board[16]==char and board[26]==char and board[36]==char) or
           (board[11]==char and board[21]==char and board[31]==char) or
           (board[12]==char and board[22]==char and board[32]==char) or
           (board[13]==char and board[23]==char and board[33]==char) or
           (board[17]==char and board[25]==char and board[33]==char) or
           (board[11]==char and board[25]==char and board[39]==char) or
           (board[13]==char and board[25]==char and board[37]==char) or
           (board[19]==char and board[25]==char and board[31]==char))
#cross board conditions


 
    
    
