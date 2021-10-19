# write your code here

def read_input():
    input_ = input('Enter cells:')
    return input_


def gen_board(input_):
    input_ = [x for x in input_]
    board = []
    for i in range(0, 9, 3):
        board.append(input_[i:i + 3])
    return board


def print_board(board):
    print('---------')
    for el in board:
        print('| ' + ' '.join(el) + ' |')
    print('---------')


def check_state(board):
    win_board = []

    def get_winning(el):
        """Takes el as list and count if """
        if el.count('X') == 3:
            return 'X'
        if el.count('O') == 3:
            return 'O'

    for pos, el in enumerate(board):
        win = get_winning(el)  # checks if theres win in line
        win_board.append(win) if win is not None else None  # appends win board if theres win
        column = [row[pos] for row in board]  # gens column
        win = get_winning(column)  # checks if theres win in column
        win_board.append(win) if win is not None else None  # appends win board if theres win
    main_diagonal = [board[0][0], board[1][1], board[2][2]]  # gens main diagonal
    win = get_winning(main_diagonal)  # checks if theres win in main diagonal
    win_board.append(win) if win is not None else None  # appends win board if theres win
    anti_diagonal = [board[2][0], board[1][1], board[0][2]]  # gens anti diagonal
    win = get_winning(anti_diagonal)# checks if theres win in anti diagonal
    win_board.append(win) if win is not None else None # appends win board if theres win
    # print(win_board) # DEBUG:prints win board
    win_state = '' # holds state of win [DRAW,X WINS,O WINS]
    if win_board.count('X') == win_board.count('O'):  # checks if same both sides has same wins
        win_state = 'Draw'  #
    elif win_board.count('X') > win_board.count('O'): # checks if x has more wins than o
        win_state = 'X wins'
    elif win_board.count('X') < win_board.count('O'):# checks if o has more wins than x
        win_state = 'O wins'
    # saves state of game its absolute of dif of count x and o in input
    state = abs([x for x in input_].count('X') - [x for x in input_].count('O'))
    # print(state)  #  Debug
    if state >= 2: # if state >2
        win_state = 'Impossible'
    if win_state == 'Draw' and state >= 1 and len(win_board)>0:
        win_state = 'Impossible'
    elif state == 0 and len(win_board)==0:
        win_state = 'Game not finished'
    print(win_state)
input_  = read_input()
# input_ = 'XO_XO_XOX' # Debug
board = gen_board(input_)
print_board(board)
check_state(board)


