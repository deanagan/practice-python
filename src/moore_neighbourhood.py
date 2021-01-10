#!/usr/bin/python3
from itertools import product

Grid = tuple[tuple[int]]

def count(grid: Grid, row: int, col: int) -> int:
    nbrs = [(rowoffset,coloffset) for rowoffset, coloffset in product(range(-1,2), repeat=2) if rowoffset or coloffset]
    return sum([grid[nrow+row][ncol+col] for nrow,ncol in nbrs if 0 <= nrow+row < len(grid) and 0 <= ncol+col < len(grid[0])])