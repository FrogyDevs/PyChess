import chess

def init_board():
    global board
    board = chess.Board()
    print(board)

def move_piece(move):
    board.push_san(move)
    print(board)

def main():
    init_board()
    move_piece('e4')

    move_piece('e5')

if __name__ == '__main__':
    main()