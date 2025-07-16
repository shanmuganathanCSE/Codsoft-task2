board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def reset_board():
    global board
    board = [' ' for _ in range(9)]

def update_board(index, player):
    board[index] = player

def is_spot_empty(index):
    return board[index] == ' '

def get_board():
    return board.copy()

def get_available_moves():
    return [i for i in range(9) if board[i] == ' ']
