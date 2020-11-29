def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:

    path = []
    visited = {}
    if start not in matrix:
        return "Invalid input"

    stack = [start]
    prev = -1

    while (end not in visited) and stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited[vertex] = prev
        prev = vertex
        for index in range(len(matrix[vertex])):
            if matrix[vertex][index]:
                stack.append(index)

    if end in visited:
        vertex = end
        while visited.get(vertex) != -1:
            path.append(vertex)
            vertex = visited.get(vertex)
    path.append(start)
    path.reverse()
    print(path)
    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO:

    path = []
    visited = {}
    if start not in matrix:
        return "Invalid input"

    queue = [start]
    prev = -1
    while (end not in visited) and queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        visited[vertex] = prev
        prev = vertex
        for index in range(len(matrix[vertex])):
            if matrix[vertex][index]:
                queue.append(index)

    if end in visited:
        vertex = end
        while visited.get(vertex) != -1:
            path.append(vertex)
            vertex = visited.get(vertex)
    path.append(start)
    path.reverse()
    print(visited)
    return visited, path

def UCS(matrix, start, end, pos):
    """
    Uniform Cost Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path = []
    visited = {}
    return visited, path
