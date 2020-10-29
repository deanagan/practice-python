import pytest

from src.cluster_counter import count_cluster, Node

def test_neighboring_node():
    a = Node(0,0, 0)

    assert a.is_neighbor(0,1) == True, '0,0 is neighbors with 0,1'
    assert a.is_neighbor(1,0) == True, '0,0 is neighbors with 1,0'
    assert a.is_neighbor(1,1) == True, '0,0 is neighbor with 1,1'

    b = Node(1,1, 0)
    assert b.is_neighbor(0,0) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(0,1) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(0,2) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(1,0) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(1,2) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(2,0) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(2,1) == True, '1,1 is neighbor with all'
    assert b.is_neighbor(2,2) == True, '1,1 is neighbor with all'

    c = Node(1,2, 0)
    assert c.is_neighbor(0,1) == True, '1,2 is neighbors with 0,1'
    assert c.is_neighbor(0,2) == True, '1,2 is neighbors with 0,2'
    assert c.is_neighbor(1,1) == True, '1,2 is neighbor with 1,1'
    assert c.is_neighbor(2,1) == True, '1,2 is neighbor with 2,1'
    assert c.is_neighbor(2,2) == True, '1,2 is neighbor with 2,2'

def test_not_neighboring_node():
    d = Node(2,2, 0)
    assert d.is_neighbor(2,0) == False, '2,2 is not neighbors with 2,0'
    assert d.is_neighbor(0,2) == False, '2,2 is not neighbors with 0,2'


def test_count_clusters():
    assert count_cluster([[1,0,0],
                          [0,0,1],
                          [1,0,1]]) == 3

    assert count_cluster([[1,0,0],
                          [0,1,0],
                          [1,0,1]]) == 1

    assert count_cluster([[1, 1, 0, 0, 1],
                         [1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 0],
                         [1, 1, 0, 0, 0],
                         [1, 1, 0, 0, 1]]) == 5