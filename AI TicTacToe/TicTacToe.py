import random


def display_board(board):
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]  # diagonals
    ]
    return any(all(board[i] == mark for i in combination) for combination in winning_combinations)


def choose_first():
    return random.choice(['Player 1', 'Player 2'])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
    return position


def replay():
    choice = input(
