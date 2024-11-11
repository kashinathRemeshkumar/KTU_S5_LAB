def back_track_algo(graph,colors):

    def is_safe(assignment,color,node):
        for neighbor in graph[node]:
            if assignment.get(neighbor)==color:
                return False
        return True
    
    def backtrack(assignment):
        if len(graph)==len(assignment):
            return assignment
        else:
            for node in graph:
                if node not in assignment:
                    for color in colors:
                        if is_safe(assignment,color,node):
                            assignment[node]=color
                            solution=backtrack(assignment)
                            if solution:
                                return assignment
                            del(assignment[node])
                    return None
            return None
        
    return backtrack({})

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Blue', 'Green']
solution = back_track_algo(graph, colors)

# Print the result
if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"Node {node}: Color {color}")
else:
    print("No solution found")
