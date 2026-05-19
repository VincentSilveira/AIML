
graph = {
'A' : ['B','C'],
'B' : ['A','C','D'],
'C' : ['A','B','E'],
'D' : ['B','E'],
'E' : ['C','D']
}

visitedNodes = []

queueNodes = []
# function
def bfs(visitedNodes, graph, snode):
	visitedNodes.append(snode)
	queueNodes.append(snode)
	print()
	print("RESULT :")
	while queueNodes:
		s = queueNodes.pop(0)
		print (s, end = " ")
		for neighbour in graph[s]:
			if neighbour not in visitedNodes:
				visitedNodes.append(neighbour)
				queueNodes.append(neighbour)


snode = input("Enter Starting Node(A, B, C, D, or E) :").upper()

bfs(visitedNodes, graph, snode)



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
