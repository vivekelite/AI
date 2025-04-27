from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=' ')
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {}
edges = int(input("Enter number of edges: "))

for _ in range(edges):
    u, v = input("Enter edge (from to): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v) 

start_node = input("Enter start node: ")

print("\nBFS Traversal:")
bfs(graph, start_node)

print("\nDFS Traversal:")
dfs(graph, start_node)
