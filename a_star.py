import heapq


def heuristic(start, goal):
    if start == goal:
        return 0
    else:
        return 1

def a_star(graph, start, goal):
    # Queue : F_score, G_score, current_node, path taken
    queue = [(heuristic(start,goal), 0, start, [start])]

    # # g_score is dictonary that consist of node: value
    # g_scores = {node: float('inf') for node in graph}
    g_scores = {}
    for nodes in graph:

        g_scores[nodes] = float('inf')

    g_scores[start] = 0

    while queue:
        f_score, g_score, curr_node, path = heapq.heappop(queue)

        if curr_node == goal:
            return  path

        for neighbour in graph[curr_node]:
            tentative_g = g_score+1

            if g_scores[neighbour] > tentative_g:
                g_scores[neighbour] = tentative_g
                # g(n) + f(n)
                f_score = tentative_g + heuristic(start, goal)
                new_path = path + [neighbour]

                heapq.heappush(queue, (f_score, tentative_g, neighbour, new_path))

    return  None



if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'E'],
        'D': ['B', 'E'],
        'E': ['C', 'D']
    }

    res = a_star(graph, 'A', 'E')
    print(res)