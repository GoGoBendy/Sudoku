"""
This module generates a Sudoku puzzle by ensuring no duplicate numbers in any row.
"""

import random
import sys

sys.setrecursionlimit(250000)


def listchecker(obj1, others):
    """
    Checks if any element in obj1 is duplicated in the same position in any of the other lists.
    If a duplicate is found, it regenerates obj1.
    """
    for i in range(9):
        if any(obj1[i] == other[i] for other in others):
            obj1 = numchecker(obj1, others)
    return obj1


def numchecker(lis1, others):
    """
    Regenerates lis1 if any element is duplicated in the same position in any of the other lists.
    """
    for i in range(9):
        if any(lis1[i] == other[i] for other in others):
            lis1 = random.sample(baserow, k=len(baserow))
            return listchecker(lis1, others)
    return lis1


baserow = [1, 2, 3, 4, 5, 6, 7, 8, 9]

row1 = random.sample(baserow, k=len(baserow))
row2 = random.sample(baserow, k=len(baserow))
row2 = numchecker(row2, [row1])
row3 = random.sample(baserow, k=len(baserow))
row3 = numchecker(row3, [row1, row2])

row4 = random.sample(baserow, k=len(baserow))
row4 = numchecker(row4, [row1, row2, row3])

row5 = random.sample(baserow, k=len(baserow))
row5 = numchecker(row5, [row1, row2, row3, row4])

row6 = random.sample(baserow, k=len(baserow))
row6 = numchecker(row6, [row1, row2, row3, row4, row5])

row7 = random.sample(baserow, k=len(baserow))
row7 = numchecker(row7, [row1, row2, row3, row4, row5, row6])

row8 = random.sample(baserow, k=len(baserow))
row8 = numchecker(row8, [row1, row2, row3, row4, row5, row6, row7])
