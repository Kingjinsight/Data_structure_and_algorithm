import heapq
def dijkstra_efficient(graph, start_node):
    d = {node: float('inf') for node in graph}
    pi = {node: None for node in graph}
    
    d[start_node] = 0
    pritority_queue = [(0, start_node)]

    while pritority_queue:
        current_dist, u = heapq.heappop(pritority_queue)
        
        if current_dist > d[u]:
            continue

        for v, weight in graph[u]:
            distance = d[u] + weight
            if distance < d[v]:
                d[v] = distance
                pi[v] = u
                heapq.heappush(pritority_queue, (distance, v))
    
    return d, pi

# --- 示例用法 ---
example_graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('D', 2)],
    'C': [('B', 4), ('D', 8), ('E', 2)],
    'D': [('E', 5)],
    'E': [('D', 1)]
}

distances, precursors = dijkstra_efficient(example_graph, 'A')
print(f"各节点最短距离: {distances}")
