import heapq

def best_first_search_tsp(graph, start):
    n = len(graph)
    priority_queue = [(0, start, [start])]
    best_cost = float('inf')
    best_path = []
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        print(f"Step: Visited {path} with cost {cost}")
        
        if len(path) == n:
            total_cost = cost + graph[node][start]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [start]
            continue
        
        for neighbor in range(n):
            if neighbor not in path:
                heapq.heappush(priority_queue, (cost + graph[node][neighbor], neighbor, path + [neighbor]))
    
    print(f"Best Path: {best_path} with Cost: {best_cost}")
    return best_path, best_cost

# Example graph (Adjacency Matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Solving TSP using Best First Search:")
best_first_search_tsp(graph, 0)
