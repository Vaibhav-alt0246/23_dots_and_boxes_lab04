import unittest

from board import Board


class AddLineValidationTests(unittest.TestCase):
    def test_line_dimensions_match_board_size(self):
        board = Board(rows=3, cols=3)

        self.assertEqual(board.line_dimensions("H"), (4, 3))
        self.assertEqual(board.line_dimensions("V"), (3, 4))

    def test_rejects_invalid_orientation(self):
        board = Board()

        with self.assertRaises(ValueError):
            board.add_line("D", 0, 0)

        self.assertFalse(any(map(any, board.horizontal)))
        self.assertFalse(any(map(any, board.vertical)))

    def test_rejects_negative_coordinates(self):
        board = Board()

        with self.assertRaises(ValueError):
            board.add_line("H", -1, 0)
        with self.assertRaises(ValueError):
            board.add_line("V", 0, -1)

    def test_rejects_out_of_range_coordinates_for_each_orientation(self):
        board = Board(rows=2, cols=2)

        with self.assertRaises(ValueError):
            board.add_line("H", board.rows + 1, 0)
        with self.assertRaises(ValueError):
            board.add_line("H", 0, board.cols)
        with self.assertRaises(ValueError):
            board.add_line("V", board.rows, 0)
        with self.assertRaises(ValueError):
            board.add_line("V", 0, board.cols + 1)

    def test_rejects_repeated_line(self):
        board = Board()
        board.add_line("H", 0, 0)

        with self.assertRaises(ValueError):
            board.add_line("H", 0, 0)


if __name__ == "__main__":
    unittest.main()
