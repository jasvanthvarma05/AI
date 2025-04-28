def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column numbers 0-2): ").split())
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move, please enter row and column numbers between 0 and 2.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        player_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

tic_tac_toe()
