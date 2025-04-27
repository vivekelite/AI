def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node]) 
    return parent[node]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(edges, nodes):
    parent = {}
    rank = {}
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            total_cost += weight

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print(f"Total minimum cost: {total_cost}")


edges = []
nodes = set()

n = int(input("Enter number of edges: "))

print("Enter edges in format: from_node to_node cost")
for _ in range(n):
    u, v, w = input().split()
    w = int(w)
    edges.append((u, v, w))
    nodes.add(u)
    nodes.add(v)

kruskal(edges, nodes)
