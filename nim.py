import sys

def next_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1

def initial():
    return [5, 4, 3, 2, 1]

def finished(board):
    return all(stars == 0 for stars in board)

def valid(board, row, num):
    if row == 0 or row > 5:
        return False
    elif board[row - 1] == 0 or board[row - 1] < num:
        return False
    else:
        return board[row - 1] >= num

def move(board, row, num):
    new_board = board[:]
    new_board[row - 1] -= num
    return new_board

def put_row(row, num):
    print(f"{row}: {'* ' * num}")

def put_board(board):
    for i, num in enumerate(board, start=1):
        put_row(i, num)

def get_digit(prompt):
    while True:
        try:
            x = input(prompt)
            if x.isdigit():
                return int(x)
            else:
                print("ERROR: Invalid digit")
        except EOFError:
            sys.exit(0)

def play(board, player):
    print()
    put_board(board)
    if finished(board):
        print()
        print(f"Player {next_player(player)} wins!")
    else:
        print()
        print(f"Player {player}")
        row = get_digit("Enter a row number: ")
        num = get_digit("Stars to remove: ")
        if valid(board, row, num):
            play(move(board, row, num), next_player(player))
        else:
            print()
            print("ERROR: Invalid move")
            play(board, player)

def nim():
    play(initial(), 1)

nim()