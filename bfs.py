"""
Implementation of breadth first search in python on graphs 
"""

graph = {
    'A' : ['B', 'C'], 
    'B' : ['D', 'E', 'C'], 
    'C' : ['I','F'],
    'D': [], 
    'E': ['F', 'I'], 
    'F': ['G', 'H']
}

visited = [] # list to keep track of visited nodes 
queue = []  # initialize a queue 

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue: 
        s = queue.pop(0) # First in First out 
        print (s, end = " ")

        for neighbour in graph[s]: #TODO: check the neighbour in each node
            if neighbour not in visited: 
                visited.append(neighbour)
                queue.append(neighbour)
            

print(bfs(visited, graph, 'A'))



