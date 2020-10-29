
from typing import List, Tuple
ClusterMap = List[List[int]]

class Node:
    def __init__(self, x: int, y: int, cluster_id: int):
        self._x = x
        self._y = y
        self.id = cluster_id

    def is_neighbor(self, x: int, y: int) -> bool:
        row_dist = abs(self._x - x)
        col_dist = abs(self._y - y)
        return row_dist < 2 and col_dist < 2

def get_next_node(clusters: ClusterMap) -> Tuple[int, int, int]:
    for row, row_elements in enumerate(clusters):
        for col, n in enumerate(row_elements):
            yield (row, col, n)

def count_cluster(clusters: ClusterMap) -> int:
    node_id = 0
    nodes = {}
    for row, col, n in get_next_node(clusters):
        if n == 1:
            neighbor = next((v for n in nodes.values() for v in n if v.is_neighbor(row,col)), None)
            nodes.setdefault(cluster_id := neighbor.id if neighbor else node_id, []).append(Node(row, col, cluster_id))
            if not neighbor:
                node_id += 1

    return len(nodes.keys())
