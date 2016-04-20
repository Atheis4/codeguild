class ListListTTTBoard:
    def __init__(self):
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, player):
        self.rows[y][x] = player

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""

        master_list = []
        diag_list = [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],[self.rows[0][2], self.rows[1][1], self.rows[2][0]]]

        column = list(zip(*self.rows))
        column = [list(x) for x in column]
        master_list += self.rows
        master_list += column
        master_list += diag_list

        if ['X','X','X'] in master_list:
            return 'X'
        elif ['O', 'O', 'O'] in master_list:
            return 'O'
        else:
            return None

    def __str__(self):
        return '{}\n{}\n{}\n'.format(
            '|'.join(self.rows[0]),
            '|'.join(self.rows[1]),
            '|'.join(self.rows[2])
        )

class DictTTTBoard:
    """Tic-Tac-Toe board that implements storage as a flat
    dictionary of slots."""

    def __init__(self):
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, token):
        if x == 0:
            x_val = 'a'
        elif x == 1:
            x_val = 'b'
        else:
            x_val = 'c'

        if y == 0:
            y_val = '1'
        if y == 1:
            y_val = '2'
        if y == 2:
            y_val = '3'

        dict_key = x_val + y_val
        self.pos_to_token[dict_key] = token

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""

        sorted_key_list = sorted(self.pos_to_token)
        token_list = list(map(self.pos_to_token.get, sorted_key_list))

        another_list = [token_list[i:i+3] for i in range(0, len(token_list), 3)]
        more_listing = list(zip(*another_list))
        more_listing = [list(item) for item in more_listing]
        diag_list = [[self.pos_to_token['a1'], self.pos_to_token['b2'], self.pos_to_token['c3']], [self.pos_to_token['a3'], self.pos_to_token['b2'], self.pos_to_token['c1']]
        ]

        master_list = []
        master_list += another_list
        master_list += more_listing
        master_list += diag_list

        if ['X','X','X'] in master_list:
            return 'X'
        elif ['O', 'O', 'O'] in master_list:
            return 'O'
        else:
            return None

    def __str__(self):
        """Returns a string representation of the board."""
        sorted_key_list = sorted(self.pos_to_token)
        token_list = list(map(self.pos_to_token.get, sorted_key_list))

        another_list = [token_list[i:i+3] for i in range(0, len(token_list), 3)]
        more_listing = list(zip(*another_list))

        return '{}\n{}\n{}\n'.format(
            '|'.join(more_listing[0]), '|'.join(more_listing[1]), '|'.join(more_listing[2])
        )

class CoordsTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list of x, y, token triplets."""

    def __init__(self):
        """Initalizes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates."""
        self.x_y_token_triplets.append((x, y, player))

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        X_val_x = []
        X_val_y = []
        O_val_x = []
        O_val_y = []


        for x, y, token in self.x_y_token_triplets:
            if token == 'X':
                X_val_x.append(x)
                X_val_y.append(y)
            else:
                O_val_x.append(x)
                O_val_y.append(y)

        if X_val_x.count(0) == 3 or X_val_y.count(0) == 3:
            return 'X'
        elif X_val_x.count(1) == 3 or X_val_y.count(1) == 3:
            return 'X'
        elif X_val_x.count(2) == 3 or X_val_y.count(2) == 3:
            return 'X'
        elif len(set(X_val_x)) == 3 and len(set(X_val_y)) == 3:
            return 'X'

        elif O_val_x.count(0) == 3 or O_val_y.count(0) == 3:
            return 'O'
        elif O_val_x.count(1) == 3 or O_val_y.count(1) == 3:
            return 'O'
        elif O_val_x.count(2) == 3 or O_val_y.count(2) == 3:
            return 'O'
        elif len(set(O_val_x)) == 3 and len(set(O_val_y)) == 3:
            return 'O'
        else:
            return None

    def __str__(self):
        """Returns a string representation of the board."""
        coord_board = [[' ' for i in range(3)] for i in range(3)]
        for x, y, player in self.x_y_token_triplets:
            coord_board[y][x] = player

        return '{}\n{}\n{}\n'.format(
            '|'.join(coord_board[0]),
            '|'.join(coord_board[1]),
            '|'.join(coord_board[2])
        )

def play(board):
    """Plays a test game on an empty board. Asserts that the board is working properly."""
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    assert str(board) == "O|X| \n |X| \n | | \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'

def main():
    board1 = DictTTTBoard()
    play(board1)
    board2 = ListListTTTBoard()
    play(board2)
    board3 = CoordsTTTBoard()
    play(board3)

main()
