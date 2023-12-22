from board import Board  # Assuming your Board class is in a file named 'board.py'

def main():
    # Create an instance of the Board class
    game_board = Board()

    # Display the initial state of the board
    print("Initial Board:")
    game_board.display_board()

    # Make a move (example: player 'X' places a piece at row 3, column 4)
    game_board.make_move(2, 3, Board.Black)

    # Display the board after the move
    print("\nBoard after a move:")
    game_board.display_board()

    # Make more moves and display the board
    # ...

    # You can continue making moves and testing the board

if __name__ == "__main__":
    main()
