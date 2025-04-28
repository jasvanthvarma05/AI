import math

player = 'X'
opponent = 'O'

def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            elif board[row][0] == opponent:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10

    return 0

def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return True
    return False

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = player
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[row][col] = '-'
        return best

    else:
        best = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = opponent
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[row][col] = '-'
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = player
                move_val = minimax(board, 0, False)
                board[row][col] = '-'

                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val

    return best_move

board = [
    ['X', 'O', 'X'],
    ['-', 'O', '-'],
    ['-', '-', '-']
]

best_move = find_best_move(board)
print(f"The best move for player 'X' is: Row = {best_move[0]}, Col = {best_move[1]}")
