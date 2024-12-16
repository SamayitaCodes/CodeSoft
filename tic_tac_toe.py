# Tic Tac Toe game in Python

board = [' ' for _ in range(9)]  # Initialize an empty board

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Your turn, Player {}".format(number))

    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[choice - 1] == ' ':
                board[choice - 1] = icon
                break
            else:
                print("That space is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def is_victory(icon):
    # Check rows, columns, and diagonals for a win
    return (
        (board[0] == icon and board[1] == icon and board[2] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        (board[0] == icon and board[3] == icon and board[6] == icon) or
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[0] == icon and board[4] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon)
    )

def is_tie():
    return ' ' not in board

# Main game loop
while True:
    print_board()
    player_move('X')
    if is_victory('X'):
        print_board()
        print("Player 1 wins! Congratulations!")
        break
    if is_tie():
        print_board()
        print("It's a tie!")
        break

    print_board()
    player_move('O')
    if is_victory('O'):
        print_board()
        print("Player 2 wins! Congratulations!")
        break
    if is_tie():
        print_board()
        print("It's a tie!")
        break
