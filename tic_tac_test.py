import tic_tac
import unittest

class Board(unittest.TestCase):
    def test_place_list(self):
        board1 = tic_tac.ListListTTTBoard()
        board1.place(1, 2, 'X')
        assert board1.rows[2][1] == 'X'

    def test_won(self):
        board1 = tic_tac.ListListTTTBoard()
        board1.place(1, 1, 'X')
        board1.place(1, 2, 'X')
        board1.place(1, 0, 'X')
        assert board1.won() == 'X'

    def test_won_two(self):
        board1 = tic_tac.ListListTTTBoard()
        board1.place(1, 0, 'O')
        board1.place(2, 1, 'X')
        board1.place(1, 1, 'O')
        assert board1.won() == None

    def test_won_three(self):
        board1 = tic_tac.ListListTTTBoard()
        board1.place(2, 0, 'O')
        board1.place(1, 1, 'O')
        board1.place(0, 2, 'O')
        assert board1.won() == 'O'

    def test_place_dict(self):
        board2 = tic_tac.DictTTTBoard()
        board2.place(1, 1, 'X')
        assert board2.pos_to_token['b2'] == 'X'

    def test_won(self):
        board2 = tic_tac.DictTTTBoard()
        board2.place(0, 0, 'O')
        board2.place(1, 1, 'O')
        board2.place(2, 2, 'O')
        assert board2.won() == 'O'

    def test_won_two(self):
        board2 = tic_tac.DictTTTBoard()
        board2.place(0, 0, 'X')
        board2.place(0, 1, 'X')
        board2.place(0, 2, 'X')
        assert board2.won() == 'X'

    def test_won_three(self):
        board2 = tic_tac.DictTTTBoard()
        board2.place(0, 1, 'O')
        board2.place(1, 0, 'X')
        board2.place(2, 2, 'X')
        assert board2.won() == None