def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def tied_game(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 
    
def winner_declared(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(immediate):
    if immediate == "" or immediate == "O":
        return "X"
    elif immediate == "X":
        return "O"

def main():
    player = next_player("")
    board = make_board()
    while not (winner_declared(board) or tied_game(board)):
        show_board(board)
        make_move(player, board)
        player = next_player(player)
    if winner_declared(board):
        show_board(board)
        print("Thank you for playing!") 
    elif tied_game(board):
        show_board(board)
        print("It's a tie.")

if __name__ == "__main__":
    main()