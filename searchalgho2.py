from collections import deque

# Breadth-First Search (BFS) for Number Puzzle
def bfs_number(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for next_node in (node + 1, node * 2):
                queue.append(path + [next_node])

    return None


# Depth-First Search (DFS) for Number Puzzle
def dfs_number(start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    node = path[-1]

    if node == goal:
        return path

    visited.add(node)

    for next_node in (node + 1, node * 2):
        if next_node not in visited:
            new_path = dfs_number(start, goal, path + [next_node], visited)
            if new_path:
                return new_path

    return None


# Run the algorithms
print("BFS Path to 10:", bfs_number(1, 10))
print("DFS Path to 10:", dfs_number(1, 10))
