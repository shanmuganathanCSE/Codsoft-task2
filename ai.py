import math
from board import update_board, get_available_moves, is_spot_empty, get_board
from game import check_winner, is_draw

def minimax(is_maximizing, alpha, beta):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for move in get_available_moves():
            update_board(move, 'O')
            score = minimax(False, alpha, beta)
            update_board(move, ' ')
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for move in get_available_moves():
            update_board(move, 'X')
            score = minimax(True, alpha, beta)
            update_board(move, ' ')
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in get_available_moves():
        update_board(i, 'O')
        move_val = minimax(False, -math.inf, math.inf)
        update_board(i, ' ')
        if move_val > best_val:
            best_val = move_val
            move = i
    return move
