# write your code here

def read_input():
    input_ = input('Enter cells:')
    return input_


def gen_board():
    board = [['_' for i in range(3)] for j in range(3)]
    return board


def print_board(board):
    print('---------')
    for el in board:
        print('| ' + ' '.join(el) + ' |')
    print('---------')

def take_move():
    'Takes input validate it and return as list of pos'
    while True:
        input_ = input('Enter the coordinates:')
        input_ = input_.split()
        if input_[0].isdigit() and input_[1].isdigit():
            input_ = [int(x)-1 for x in input_]
            if all([x in range(3) for x in input_]):

                if ('X' in board[input_[0]][input_[1]]) or ("O" in board[input_[0]][input_[1]]):
                    print("This cell is occupied! Choose another one!")
                else:
                    return input_
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
def insert_move(board,pos,identyfier):
    board[pos[0]][pos[1]] = identyfier
def check_state(board):
    win_board = []
    input_ = ''.join([y for x in board for y in x])
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
    print('win obard',win_board) # DEBUG:prints win board
    win_state = False # holds state of win [DRAW,X WINS,O WINS]
    if len(win_board)!=0:
        if win_board.count('X') == win_board.count('O'):  # checks if same both sides has same wins
            win_state = 'Draw'  #
        elif win_board.count('X') > win_board.count('O'): # checks if x has more wins than o
            win_state = 'X wins'
        elif win_board.count('X') < win_board.count('O'):# checks if o has more wins than x
            win_state = 'O wins'
    # saves state of game its absolute of dif of count x and o in input
    state = abs([x for x in input_].count('X') - [x for x in input_].count('O'))
    print('state:',state)  #  Debug
    if state >= 2: # if state >2
        win_state = '1Impossible'
    if len(win_board)>=  and state == 1:
        win_state = '2Impossible'
    elif len(win_board)==0 and state < 1:
        pass
    return win_state
# input_  = read_input()
# input_ = 'X_X_O____' # Debug
board = gen_board()
# board = [['X','O','X'],['X','O','X'],['O','X','O']]
# print(check_state(board))
# print_board(board)
while True:
    tokens = ['X','O']
    for el in tokens:
        print_board(board)
        next_move = take_move()
        insert_move(board,next_move,el)
        win_state = check_state(board)
        if win_state:
            print_board(board)
            print(win_state)
            break
    if win_state:
        break


