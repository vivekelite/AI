import heapq

def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        if cost != 0:  
            mst_edges.append((prev_node, node, cost))

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))
        
        prev_node = node  
    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} : {w}")
    print(f"Total minimum cost: {total_cost}")

# Taking input
graph = {}
edges = int(input("Enter number of edges: "))

print("Enter edges in format: from_node to_node cost")
for _ in range(edges):
    u, v, cost = input().split()
    cost = int(cost)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, cost))
    graph[v].append((u, cost)) 

start = input("Enter starting node: ")

prims_algorithm(graph, start)