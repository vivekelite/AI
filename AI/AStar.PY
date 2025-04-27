import heapq

def heuristic(a, b):
    return 0 

def a_star_search(start, goal, graph):
    heap = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while heap:
        current_priority, current = heapq.heappop(heap)

        if current == goal:
            break

        for neighbor, weight in graph.get(current, []):
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(heap, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from.get(node)
        if node is None:
            print("No path found!")
            return
    path.append(start)
    path.reverse()

    print("Path found:", path)
    print("Total cost:", cost_so_far[goal])


graph = {}
edges = int(input("Enter number of edges: "))

print("Enter edges in format: from_node to_node cost")
for _ in range(edges):
    u, v, cost = input().split()
    cost = int(cost)
    if u not in graph:
        graph[u] = []
    graph[u].append((v, cost))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star_search(start, goal, graph)
