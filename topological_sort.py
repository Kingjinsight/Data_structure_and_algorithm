# the graph must be a DAG(Directed acyclic graph)
def topological_sort(graph):
    stack=[]
    visited=set()

    def dfs(node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]

