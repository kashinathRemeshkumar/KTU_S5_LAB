def bfs(graph,goal,start):
    queue=[start]
    visited=[start]
    parent={start:None}

    while queue:
        current_node=queue.pop(0)
        if current_node==goal:
            break
        else:
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    parent[neighbour]=current_node
                    queue.append(neighbour)
                    visited.append(neighbour)

    path=[]
    if goal in visited:
        current=goal
        while current is not None:
            path.append(current)
            current=parent[current]
        path.reverse()
        return path
    else:
        return "no path exists"

graph={
    'A':['B','C'],
    'B':['D','E'],
    'D':[],
    'E':[],
    'G':[],
    'C':['F','G'],
    'F':[]
}

print(bfs(graph,'G','A'))
                
