'''TicTacToe'''
def tictactoe():
    '''Func. tictactoe for input tictactoe'''
    line_1, line_2, line_3 = input(), input(), input()
    final = line_1 + line_2 + line_3
    if final[:3] == 'OOO' or final[3:6] == 'OOO' or\
    final[6:9] == 'OOO' or final[0] + final[3] + final[6] == 'OOO' or\
    final[1] + final[4] + final[7] == 'OOO' or final[2] + final[5] + final[8] == 'OOO' or\
    final[0] + final[4] + final[8] == 'OOO' or final[2] + final[4] + final[6] == 'OOO':
        print('O WIN')
    elif final[:3] == 'XXX' or final[3:6] == 'XXX' or final[6:9] == 'XXX' or\
    final[0] + final[3] + final[6] == 'XXX' or final[1] + final[4] + final[7] == 'XXX' or\
    final[2] + final[5] + final[8] == 'XXX' or final[0] + final[4] + final[8] == 'XXX' or\
    final[2] + final[4] + final[6] == 'XXX':
        print('X WIN')
    else:
        print('DRAW')
tictactoe()
