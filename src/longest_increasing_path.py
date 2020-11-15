from itertools import product, takewhile
from typing import List, Tuple
from collections import deque


Matrix = List[List[int]]
class MatrixRunner:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

    def neighbors(self, location, rows, cols):
        current_row, current_col = location
        yield from [(current_row + r, current_col + c) for r,c in [(0,1), (1,0), (0,-1), (-1,0)]
                    if 0 <= (current_row + r) < rows and
                       0 <= (current_col + c) < cols]

    def longest_path(self):
        cache, visited, lengths = {}, {}, []

        for row, col in product(range(self.n_rows), range(self.n_cols)):
            lengths.append(self.depth_first_search((row, col), cache, visited))

        return max(lengths)

    def depth_first_search(self, location, cache, visited):
        visited[location] = True
        location_value = self.matrix[location[0]][location[1]]

        for n in self.neighbors(location, self.n_rows, self.n_cols):
            n_value = self.matrix[n[0]][n[1]]
            if location_value < n_value and n_value not in visited:
                return 1 + self.depth_first_search(n, cache, visited)

        return 1



def longest_increasing_path(matrix: Matrix) -> int:

    mr = MatrixRunner(matrix)
    return mr.longest_path()
