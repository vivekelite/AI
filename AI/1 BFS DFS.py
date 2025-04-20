# DFS BFS
def create_graph(num_vertices):
    graph = {}
    for vertex in range(num_vertices):
        graph[vertex] = []
    return graph

def add_edge(graph,vertex1,vertex2):
    if vertex1 not in graph:
        graph[vertex1]=[]
    if vertex2 not in graph:
        graph[vertex2]=[]
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

def dfs_recursive(graph,vertex,visited):
    visited.add(vertex)
    print(vertex , end=" ")
    for neighbour in graph [vertex]:
        if neighbour not in visited:
            dfs_recursive(graph,neighbour,visited)

def bfs_recursive(graph , vertex , visited , queue):
    visited.add(vertex)
    queue.append(vertex)
    while queue:
        vertex = queue.pop(0)
        print(vertex , end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():

    num_vertices = int(input("Enter the number of vertices : "))
    graph=create_graph(num_vertices)

    num_edges=int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        vertex1,vertex2 = map(int,input("Enter two vertices for an ede (space - seprated):").split())
        add_edge(graph,vertex1,vertex2)

    print("Depth-First-Search(DFS): ")
    visited =set()
    dfs_recursive(graph,1,visited)
    print("\nBreadth-First-Search(BFS):")
    visited = set()
    queue=[]
    bfs_recursive(graph , 1 , visited , queue)

if __name__ == "__main__":
    main()

