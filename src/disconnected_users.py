

class Node:
    def __init__(self, name, user_count):
        self._name = name
        self._connected_to = []
        self._user_count = user_count

    def add_connection(self, node):
        self._connected_to.append(node)

    def children(self):
        return iter(self._connected_to)

    def __add__(self, other):
        return self.user_count + other.user_count

    def __repr__(self):
        return f'Node {self._name}: Total {self._user_count} : Connections {self._connected_to}'

    @property
    def id(self):
        return self._name

    @id.setter
    def id(self, id):
        self._name = id

    @property
    def user_count(self):
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        self._user_count = user_count

def disconnected_users(net, users, source, crushes):

    # Populate all nodes
    nodes = { k: Node(k,v) for k,v in users.items() }

    # Return sum of all nodes if source is crushed
    if source in crushes:
        return sum(node.user_count for node in nodes.values())

    # Add children to each node
    for edge in net:
        node_from, node_to = edge
        nodes[node_from].add_connection(nodes[node_to])

    connected = [nodes[source],]
    visited = []
    # Add all visitable nodes
    while connected:
        node = connected.pop()
        visited.append(node.id)
        connected.extend(c for c in node.children() if c.id not in crushes)


    # Return sum of all nodes not visited
    return sum(node.user_count for node in nodes.values() if node.id not in visited)


if __name__ == "__main__":
    print(disconnected_users([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], {
            'A': 10,
            'B': 20,
            'C': 30,
            'D': 40
        },
            'A', ['C']))
