from board import get_board

def check_winner(player):
    b = get_board()
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],     
        [0, 3, 6], [1, 4, 7], [2, 5, 8],     
        [0, 4, 8], [2, 4, 6]                 
    ]
    for cond in win_conditions:
        if all(b[i] == player for i in cond):
            return True
    return False

def is_draw():
    return ' ' not in get_board()
