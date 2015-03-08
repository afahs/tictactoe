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

 
    
    
