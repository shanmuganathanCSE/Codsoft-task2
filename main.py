# main.py

from board import print_board, update_board, is_spot_empty, reset_board
from game import check_winner, is_draw
from ai import best_move

def play_game():
    print("🎮 Welcome to Unbeatable Tic-Tac-Toe!")
    print("You are X, AI is O.")
    reset_board()
    print_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or not is_spot_empty(move):
                print("❌ Invalid move. Try again.")
                continue
            update_board(move, 'X')
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        print_board()
        if check_winner('X'):
            print("🎉 You win!")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break
        print("🧠 AI is making a move...")
        ai_move = best_move()
        update_board(ai_move, 'O')
        print_board()
        if check_winner('O'):
            print("😎 AI wins! Better luck next time.")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
