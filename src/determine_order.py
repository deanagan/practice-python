from itertools import chain

class Node:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.children = []

    def add_child(self, node):
        if node not in self.children and node != self:
            self.children.append(node)

    def __repr__(self):
       children = ','.join(i.name for i in self.children if i)
       return f'Node: {self.name} priority: {self.priority}, children: [{children}]'


def update_priority(node, priority):
    node.priority = max(priority + 1, node.priority)
    for child in node.children:
        update_priority(child, node.priority)

def determine_order(items):
    char_lot = ''.join(sorted(chain.from_iterable(items)))
    if all(a==b for a,b in zip(sorted(set(char_lot)),char_lot)):
        return char_lot

    nodes = {}
    for word in items:
        for i, ch in enumerate(word):
            nodes[ch] = nodes.get(ch, Node(ch, i))
            if i > 0:
                nodes[word[i-1]].add_child(nodes[ch])
                update_priority(nodes[ch], nodes[word[i-1]].priority)

    return ''.join(e.name for e in  sorted(nodes.values(), key=lambda n: (n.priority, ord(n.name)) ))
