import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinite distance
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to get the node with the smallest distance
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If a shorter path is found, skip processing
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If the new distance is shorter, update the shortest path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Taking input
nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

graph = {}

# Initialize empty lists for each node
for _ in range(nodes):
    node = input("Enter node name: ")
    graph[node] = []

print("Enter edges in format: from_node to_node weight")
for _ in range(edges):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))  # Assuming undirected graph

start_node = input("Enter start node: ")

# Run Dijkstra's algorithm
distances = dijkstra(graph, start_node)

# Display the shortest distances
print("\nShortest distances from the start node:")
for node, distance in distances.items():
    print(f"{start_node} to {node}: {distance}")
