

from collections import deque
from itertools import tee, chain
from itertools import count
from operator import add

class Node:
    instance_counter = count(0)
    def __init__(self, name, priority):
        self.id = next(Node.instance_counter)
        self.name = name
        self.parent = None
        self.priority = priority
        self.children = []

    def add_predecessor(self, node):
        self.parent = min(node, self.parent, key=lambda np: np.id) if self.parent else node


    def add_child(self, node):
        if node not in self.children and node != self:
            self.children.append(node)


    def __repr__(self):
        parent = self.parent.name if self.parent else 'no parent'
        children = ','.join(i.name for i in self.children if i)
        return f'Node: {self.name} id: {self.id} priority: {self.priority} parent: {parent}, children: [{children}]'


def update_priority(node, priority):
    node.priority = priority + 1
    for i, c in enumerate(node.children, start=1):
        c.priority += (node.priority + i)
        update_priority(c, c.priority)



def determine_order(items):
    nodes = {}
    for wi, word in enumerate(items):
        for i, ch in enumerate(word):
            nodes[ch] = nodes.get(ch, Node(ch, wi+i))
            if i > 0:
                nodes[ch].add_predecessor(nodes[word[i-1]])
                nodes[word[i-1]].add_child(nodes[ch])
                update_priority(nodes[ch], nodes[word[i-1]].priority)
    print(*nodes.values(), sep='\n')
    return ''.join(e.name for e in  sorted(nodes.values(), key=lambda n: n.priority ))



if __name__ == '__main__':
    assert determine_order(["axton","bxton"]) == "abxton"



    # assert determine_order(["acb", "bd", "zwa"])  == "zwacbd"
    # assert determine_order(["klm", "kadl", "lsm"])  == "kadlsm"
    # assert determine_order(["a", "b", "c"])  == "abc"
    # assert determine_order(["aazzss"])  == "azs"

    # assert determine_order(["dfg", "frt", "tyg"])  == "dfrtyg"
    # assert determine_order(["xxxyyz", "yyww", "wwtt", "ttzz"])  == "xywtz"

    #assert determine_order(["jhgfdba","jihcba","jigedca"]) == "jihgefdcba"
