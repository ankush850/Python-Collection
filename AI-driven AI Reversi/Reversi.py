import copy

# Reversi Board Size
BOARD_SIZE = 8

# Define player colors
EMPTY = 0
BLACK = 1
WHITE = 2

# Define directions to explore in the board
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        print(f"{i} |" + " ".join(str(board[i][j]) for j in range(BOARD_SIZE)))


def is_valid_move(board, player, row, col):
    if board[row][col] != EMPTY:
        return False

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] != EMPTY and board[r][c] != player:
            r, c = r + dr, c + dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                return True
    return False


def make_move(board, player, row, col):
    if not is_valid_move(board, player, row, col):
        return False

    board[row][col] = player
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        to_flip = []
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] != EMPTY and board[r][c] != player:
            to_flip.append((r, c))
            r, c = r + dr, c + dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                for flip_row, flip_col in to_flip:
                    board[flip_row][flip_col] = player
                break
    return True


def get_valid_moves(board, player):
    valid_moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if is_valid_move(board, player, i, j):
                valid_moves.append((i, j))
    return valid_moves


def count_discs(board):
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count, white_count


def evaluate_board(board, player):
    black_count, white_count = count_discs(board)
    if player == BLACK:
        return black_count - white_count
    else:
        return white_count - black_count


def minimax(board, depth, player, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board, player)

    valid_moves = get_valid_moves(boar
