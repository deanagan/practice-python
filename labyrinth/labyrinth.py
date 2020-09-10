# The labyrinth has no walls, but pits surround the path on each side. 
# If a players falls into a pit, they lose. The labyrinth is presented as 
# a matrix (a list of lists): 1 is a pit and 0 is part of the path. The labyrinth's 
# size is 12 x 12 and the outer cells are also pits. Players start at cell (1,1). 
# The exit is at cell (10,10). You need to find a route through the labyrinth. 
# Players can move in only four directions--South (down [1,0]), North (up [-1,0]), 
# East (right [0,1]), West (left [0, -1]). The route is described as a string 
# consisting of different characters: "S"=South, "N"=North, "E"=East, and "W"=West.

from collections import deque

def checkio(labmap):
    checkpoints = deque()
    compass = {'E':[0,1], 'S':[1,0], 'W':[0,-1], 'N':[-1,0]}
    visited = []
    visited.append([1,1])
    checkpoints.append([1,1])
    
    # Do breadth-first-search
    while checkpoints:
        dest = checkpoints.pop()
        for direction in compass.values():
            next_dest = list(dest+direction for dest,direction in zip(dest,direction))
            if labmap[dest[0] + direction[0]][dest[1] + direction[1]] == 0 and next_dest not in visited:
                visited.append(next_dest)

                if next_dest == [10,10]:
                    checkpoints.clear()
                    break
                else:
                    checkpoints.append(next_dest)
        
    # In reverse, determine path by tracing backward 
    location = [10,10]
    for next_location in reversed(visited[:-1]):
        if sum (abs(row-col) for row,col in zip(location,next_location)) > 1: visited.remove(next_location)
        else: location = next_location

    # Convert to directions
    routelist = []
    for parents, children in zip( visited[:-1], visited[1:] ):
        routelist.append(list(direction for direction, difference in compass.items() if [c-p for p,c in zip(parents, children)] == difference))

   
    return ''.join(routelist[t][0] for t in range(len(routelist)))
        
        
if __name__ == '__main__':
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
    #be careful with infinity loop
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
##no route
    print(checkio([[1,1,1,1,1,1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,0,0,0,0,0,1],
                   [1,0,1,1,1,1,1,1,1,1,0,1],
                   [1,0,1,0,0,0,0,0,0,1,0,1],
                   [1,0,1,0,1,1,1,1,1,1,0,1],
                   [1,0,1,0,1,0,0,0,0,1,0,1],
                   [1,0,0,0,1,1,0,1,1,1,0,1],
                   [1,0,1,0,0,0,0,1,0,1,1,1],
                   [1,0,1,1,0,1,0,0,0,0,0,1],
                   [1,0,1,0,0,1,1,1,1,1,0,1],
                   [1,0,0,0,1,1,0,0,0,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1,1]]))


    print(checkio([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))

    print(checkio([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
