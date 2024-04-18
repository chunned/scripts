# MAZE is an adjacency matrix represented as a 2D array
MAZE = [
    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]]


def getNodes():
    # Get start and end nodes with input()
    start_node = input("Please enter the starting node: ")
    end_node = input("Please enter the end node: ")
    # Map user input to a tuple
    start_node = tuple(map(int, start_node.split(",")))
    end_node = tuple(map(int, end_node.split(",")))
    return start_node, end_node


def manhattanDistance(a, b):
    # Return the Manhattan distance between a and b, where a and b are tuples of the format (x, y), with
    # x representing the outer index of the node in MAZE and y representing the inner index of the node in MAZE
    # e.g., MAZE[2][4] = (2, 4)
    xDist = abs(b[0] - a[0])
    yDist = abs(b[1] - a[1])

    # Check for blocked spaces along the x and y axes
    xBlocked = 0
    yBlocked = 0
    # Iterate over the outer indices between the node with the smaller x value and the one with the larger x value
    # If that element = 0, the position is blocked
    for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
        if MAZE[i][a[1]] == 0:
            xBlocked += 1
    # Repeat for inner indices
    for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        if MAZE[b[0]][j] == 0:
            yBlocked += 1

    # Determine which axis has fewer blocked spaces and move in that direction first
    if xDist == 0 or (yDist > 0 and yBlocked < xBlocked):
        # Move along y axis first
        yStep = 1 if b[1] > a[1] else -1
        for j in range(1, yDist + 1):
            x = b[0]
            y = a[1] + j * yStep
            if MAZE[x][y] == 0:
                yDist += 2
        manhattan = xDist + yDist
    else:
        # Move along x axis first
        xStep = 1 if b[0] > a[0] else -1
        for i in range(1, xDist + 1):
            y = a[1]
            x = a[0] + i * xStep
            if MAZE[x][y] == 0:
                xDist += 2
        manhattan = xDist + yDist
    return manhattan


def getAdjacencies(path, end):
    # Last element in the path is where we currently are
    start = path[-1]
    start_x = start[0]
    start_y = start[1]
    adjacencies = []
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # Check the nodes to the north, south, east, and west
        new_x = start_x + x
        new_y = start_y + y
        if (new_x, new_y) in path:
            # If element is already in path, it has already been visited - don't check it again
            pass
        else:
            # We cannot have negative indices, so we check that both x and y are greater than -1
            if new_x >= 0 and new_y >= 0:
                # Index of starting node corresponds to how many moves we have made, or the distance from the origin
                distance = path.index(start) + 1
                try:
                    if MAZE[new_x][new_y] == 1:
                        # Calculate Manhattan distance for current node
                        manhattan = manhattanDistance((new_x, new_y), end)
                        # Create new dictionary item for the current node
                        node = {"position": (new_x, new_y),
                                "manhattan": manhattan,
                                "f": manhattan + distance,
                                "previous": start}
                        adjacencies.append(node)
                except IndexError:
                    # Invalid element (i.e. we have reached the end of MAZE or end of one of its sub-arrays), pass
                    pass
    return adjacencies


def tiebreak(ties, end, previous):
    # First, prefer elements with more adjacencies
    adj = []
    potential_winners = []
    for i in ties:
        # Create list of the number of adjacencies
        node_position = i['position']
        # Call getAdjacencies() with a list containing the previous element and the current node
        # Previous element is required because it is not considered an adjacency - we wouldn't move back into the
        # grid space we just came from.
        adj.append(len(getAdjacencies([previous, node_position], end)))

    # Find the element(s) with the highest number of adjacencies
    max_adjacencies = max(adj)
    for i in range(len(adj)):
        if adj[i] == max_adjacencies:
            potential_winners.append(ties[i])
    # If we only have 1 element with the highest number of adjacencies, we have found our winner
    if len(potential_winners) == 1:
        winner = potential_winners[0]
    else:
        # Next, use tiebreakers as set out in assignment document; Left > Up > Right > Down
        potential_winners.sort(key=lambda adjacent: adjacent['position'][0])  # sort by x position
        potential_winners.sort(key=lambda adjacent: adjacent['position'][1])  # sort by y position
        winner = potential_winners[0]
    return winner


def traverse(path, end):
    # Traverse the maze with the A* algorithm and find the best path from the start node to end node
    start = path[-1]
    # If last element of path = end, algorithm has finished, return path
    if start == end:
        return path

    # Try neighbouring grid spaces
    adjacencies = getAdjacencies(path, end)
    # Use a lambda function as the key function for min() to find the minimum f value
    min_f = min(adjacencies, key=lambda a: a['f'])['f']
    # Add any elements whose f is equal to min_f to a list called 'ties'
    ties = [a for a in adjacencies if a['f'] == min_f]
    if len(ties) > 1:
        winner = tiebreak(ties, end, start)
    else:
        winner = ties[0]
    path.append(winner["position"])

    traverse(path, end)
    return path


def isValid(a):    # Checks if a is a valid element of MAZE
    # We cannot have negative indices, so check if either x or y is negative
    if a[0] < 0 or a[1] < 0:
        return False
    try:
        # If MAZE element value is 1, move is valid
        if MAZE[a[0]][a[1]] == 1:
            return True
        else:
            return False
    except IndexError:
        # Invalid element (i.e. we have reached the end of MAZE or end of one of its sub-arrays)
        return False


def mazePrint(maze, path):
    mazeMatrix = maze
    for node in path:
        mazeMatrix[node[0]][node[1]] = 2

    # Create top border
    top_border = ' ' + '_' * (len(mazeMatrix[0]) * 2 + 1)
    lines = [top_border]

    for row in mazeMatrix:
        # Add left border
        line = '| '
        # Grid printing solution from https://stackoverflow.com/questions/27140144/printing-2d-array-in-a-grid
        line += ' '.join('-' if x == 0 else 'o' if x == 1 else '.' for x in row)
        # Add right border
        line += ' |'
        # Append to lines
        lines.append(line)
    # Add bottom border
    bottom_border = ' ' + '_' * (len(mazeMatrix[0]) * 2 + 1)
    lines.append(bottom_border)
    print('\n'.join(lines))


origin, finish = getNodes()

# Check if origin/end point is valid
if isValid(origin) and isValid(finish):
    mazePath = traverse([origin], finish)

    print('o = open space')
    print('- = blocked space')
    print('. = player path')
    mazePrint(MAZE, mazePath)

    print(f'Optimal path from {origin} to {finish}')
    print(mazePath)
    print(f'Maze completed in {len(mazePath)} moves.')


else:
    print('Path not found. Make sure you entered a valid start and end node.')
