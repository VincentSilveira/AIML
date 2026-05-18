
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