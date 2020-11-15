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
        longest = 0
        for row, col in product(range(self.n_rows), range(self.n_cols)):
            visited = []
            longest = max(self.depth_first_search((row, col), visited), longest)

        return longest

    def valid_neighbors(self, location, visited):
        location_value = self.matrix[location[0]][location[1]]
        for n in self.neighbors(location, self.n_rows, self.n_cols):
            if location_value < self.matrix[n[0]][n[1]] and n not in visited:
                yield n


    def depth_first_search(self, location, visited):
        visited.append(location)

        max_length = 1
        for n in  self.valid_neighbors(location, visited):
            max_length = max(max_length, 1 + self.depth_first_search(n, visited))

        return max_length


def longest_increasing_path(matrix: Matrix) -> int:
    if not matrix:
        return 0
    mr = MatrixRunner(matrix)
    return mr.longest_path()
