import numpy as np

class Board:
    White = -1
    Black = 1
    Empty = 0

    import numpy as np

class Board:
    White = -1
    Black = 1
    Empty = 0

    def __init__(self) -> None:
        self.board = np.zeros((8, 8), dtype=np.int8)
        self.initialize_board()

    def initialize_board(self):
        # Set initial pieces in the center
        self.board[3:5, 3:5] = [[self.Black, self.White], [self.White, self.Black]]

    def display_board(self):
        print("  1 2 3 4 5 6 7 8")
        for i, row in enumerate(self.board):
            print(f"{i + 1} {' '.join(self.piece_to_str(cell) for cell in row)}")

    def piece_to_str(self, piece):
        if piece == self.White:
            return 'W'
        elif piece == self.Black:
            return 'B'
        else:
            return ' '

    def is_valid_move(self, row, col, player):
        # Check if the move is within bounds and the cell is empty
        return 0 <= row < 8 and 0 <= col < 8 and self.board[row, col] == self.Empty

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col, player):
            self.board[row, col] = player
            self.flip_pieces(row, col, player)

    def flip_pieces(self, row, col, player):
        # Implement logic to flip pieces based on the Othello rules
        pass

    def get_winner(self):
        # Implement logic to determine the winner based on the Othello rules
        pass
