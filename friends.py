# We have an array of straight connections between drones.
# Each connection is represented as a string with two names
# of friends separated by hyphen. For example: "dr101-mr99"
# means what the dr101 and mr99 are friends. Your should write
# a function that allow determine more complex connection
# between drones. You are given two names also. Try to determine
# if they are related through common bonds by any depth.
# For example: if two drones have a common friends or friends
# who have common friends and so on.


from collections import deque

def bfs(head_node, network):
    visited = []
    path = deque()
    path.append(head_node)
    visited.append(head_node)

    yield head_node

    while path:
        g = path.pop()
        
        if g not in network:
            continue
        for elem in network[g]:
            if elem not in visited:
                path.append(elem)
                visited.append(elem)
                yield elem
                

def check_connection(network, first, second):

    netdict = dict()

    # generate dictionary
    for t in network:
        netdict.setdefault(t.split('-')[0], []).append(t.split('-')[1])
    
    first_network = []
    second_network = []
    for g in netdict.keys():
        temp = [i for i in bfs(g, netdict)]
        if (first in temp):
            first_network.extend(temp)

        if (second in temp):
            second_network.extend(temp)

        if (set(first_network).intersection(second_network)):
            return True
    
    # No relation found
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
##    assert check_connection(
##        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
##         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
##        "scout2", "scout3") == True, "Scout Brotherhood"
##    assert check_connection(
##        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
##         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
##        "super", "scout2") == True, "Super Scout"
##    assert check_connection(
##        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
##         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
##        "dr101", "sscout") == False, "I don't know any scouts."

    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman",
         "mr99-robin","dr101-out00","out00-nwing",),
        "dr101","mr99") == True, "blah"
