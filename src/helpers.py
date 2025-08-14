from src.data_structures import CellStatus


def generate_new_board(rows: int = 5, cols: int = 5, max_value: int = 10) -> list[list[int]]:
    """
    Generate a new board with random values.

    Args:
        rows (int): Number of rows in the board.
        cols (int): Number of columns in the board.
        max_value (int): Maximum value for the random integers.

    Returns:
        list[list[int]]: A 2D list representing the board with random integers.
    """
    from random import randint
    return [[randint(1, max_value) for _ in range(cols)] for _ in range(rows)]

def generate_empty_shadow_board(rows: int = 5, cols: int = 5) -> list[list[int]]:
    """
    Generate a shadow board initialized with CellStatus.EMPTY.

    Args:
        rows (int): Number of rows in the shadow board.
        cols (int): Number of columns in the shadow board.

    Returns:
        list[list[int]]: A 2D list representing the shadow board with CellStatus.EMPTY.
    """

    return [[CellStatus.EMPTY.value for _ in range(cols)] for _ in range(rows)]