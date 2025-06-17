# num of cells with numbers to be used to reach final result for line/row
from random import randint

NUM_OF_LINES = NUM_OF_ROWS = 5
MAX_VALUE = 9

import operator
from functools import reduce

op_map = {
    '+': operator.add,
    '*': operator.mul,
}

# TODO: should be replaced with actual data
board = [[randint(1, MAX_VALUE)] * NUM_OF_LINES for _ in range(NUM_OF_ROWS)]

