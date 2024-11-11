def dfs(graph, start, goal):
    stack = [start]
    visited=[]  # Use a set for visited to avoid duplicates
    parent = {start: None}

    while stack:
        current_node = stack.pop()
        
        # Check if current node is the goal
        if current_node == goal:
            break
        
        # If current_node hasn't been visited
        if current_node not in visited:
            visited.append(current_node)  # Mark as visited
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    parent[neighbour] = current_node

    # Build path from goal to start
    path = []
    current_node = goal
    if goal not in parent:  # Goal not reached
        return None

    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]

    path.reverse()
    return path

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
print(dfs(graph, start, goal))  # Output: ['A', 'C', 'F']
