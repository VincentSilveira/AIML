import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

def heuristic(node, goal):
    return 0 if node == goal else 1

def a_star_search(graph, start, goal):

    open_set = [(heuristic(start, goal), start)]

    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None # Path not found

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1] # Reverse path to get it from start to goal

# Main Code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()
gnode = input("Enter Goal Node (A, B, C, D, or E): ").upper()

if snode not in graph or gnode not in graph:
    print("Invalid start or goal node.")
else:
    print("\nRESULT (A* Search):")
    print("-" * 20)
    path = a_star_search(graph, snode, gnode)
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")


"""
Breadth First Search (BFS) is a graph traversal algorithm used to explore nodes level by level starting from a source node.
BFS first visits all immediate neighboring nodes before moving deeper into the graph structure.
The algorithm uses a Queue (FIFO – First In First Out) data structure to maintain traversal order.
A visited list or set is maintained to avoid revisiting nodes and to prevent infinite loops in cyclic graphs.
BFS guarantees the shortest path in an unweighted graph because nodes are explored according to distance from the source node.
The algorithm is widely used in network routing, web crawling, social networking applications, GPS navigation systems, and shortest path problems.
Time Complexity of BFS is:

O(V+E)

where:

V = Number of vertices
E = Number of edges
Space Complexity is:

O(V)

because the queue and visited list may store all vertices.

BFS is preferred when the solution is expected near the root or starting node.
"""
