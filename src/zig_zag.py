
from itertools import cycle

class ZigZag:
    def convert(self, s: str, num_rows: int) -> str:
        row_strs = {}
        index_gen = cycle([*list(range(num_rows)), *list(range(num_rows - 2,0,-1))])
        for ch in s:
            row_strs.setdefault(next(index_gen), []).append(ch)

        return ''.join(''.join(row_strs[i]) for i in row_strs.keys())
