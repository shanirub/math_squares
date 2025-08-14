# num of cells with numbers to be used to reach final result for line/row
from enum import Enum
from random import randint

NUM_OF_LINES = NUM_OF_ROWS = 5
MAX_VALUE = 9

import operator
from functools import reduce

op_map = {
    '+': operator.add,
    '*': operator.mul,
}

class CellStatus(Enum):
    EMPTY = 0 # start value
    SELECTED = 1 # selected by user: use in calculations
    DESELECTED = 2 # selected by user: do not use in calculations


class Board:
    def __init__(self, rows: int = NUM_OF_ROWS, cols: int = NUM_OF_LINES):
        # number of rows and columns in the board
        self.rows = rows
        self.cols = cols
        # board with numbers
        self.board = [[randint(1, MAX_VALUE) for _ in range(cols)] for _ in range(rows)]
        # shadow board to track cell selection status
        # initialized with CellStatus.EMPTY to indicate no cells are selected
        self.shadow_board = [[CellStatus.EMPTY for _ in range(cols)] for _ in range(rows)]

    def get_row_values(self, row: int) -> list[int]:
        """
        Get the values for a given row.

        Args:
            row (int): The row number.

        Returns:
            list[int]: A list of integer values for the row.
        """
        return self.board[row]

    def get_row_total(self, row: int, op: str) -> int:
        """
        Calculate the total for a given row based on the operation and values.

        Args:
            row (int): The row number.
            op (str): The operation to perform ('+' or '*').

        Returns:
            int: The result of applying the operation to the values.
        """
        return reduce(op_map[op], self.get_row_values(row))

    def get_column_values(self, col: int) -> list[int]:
        """
        Get the values for a given column.

        Args:
            col (int): The column number.

        Returns:
            list[int]: A list of integer values for the column.
        """
        return [self.board[row][col] for row in range(self.rows)]

    def get_column_total(self, col: int, op: str) -> int:
        """
        Calculate the total for a given column based on the operation and values.

        Args:
            col (int): The column number.
            op (str): The operation to perform ('+' or '*').

        Returns:
            int: The result of applying the operation to the values.
        """
        return reduce(op_map[op], self.get_column_values(col))

    def __eq__(self, other):
        """
        Check equality of two Board instances.

        Args:
            other (Board): Another Board instance to compare with.

        Returns:
            bool: True if both boards are equal, False otherwise.
        """
        return (self.rows == other.rows and
                self.cols == other.cols and
                self.board == other.board and
                self.shadow_board == other.shadow_board)