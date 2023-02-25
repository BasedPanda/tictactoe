def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"{player}, enter a position (0-8): ")
        if move.isdigit() and int(move) in range(9) and board[int(move)] == " ":
            valid_move = True
            return int(move)
        else:
            print("Invalid move. Please try again.")

def check_win(board):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return True
    return False

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0
    winner = None

    while not winner and " " in board:
        print_board(board)
        move = get_move(board, players[turn])
        board[move] = players[turn]
        if check_win(board):
            winner = players[turn]
        turn = (turn + 1) % 2

    print_board(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("Tie game!")

play_game()
