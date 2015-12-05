#!/usr/bin/python3
from itertools import product

def count_neighbours(grid, row, col):
    nbrs = [(rowoffset,coloffset) for rowoffset, coloffset in product(range(-1,2), repeat=2) if rowoffset or coloffset]
    return sum([grid[nrow+row][ncol+col] for nrow,ncol in nbrs if 0 <= nrow+row < len(grid) and 0 <= ncol+col < len(grid[0])])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"

    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

