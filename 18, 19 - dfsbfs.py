from collections import deque

def dfs(graph, start, end, path, shortest):
	path = path + [start]
	print(path)
	if start == end:
		return path
	for node in graph[start]:
		if node not in path:
			if shortest == None or len(path) < len(shortest):
				newpath = dfs(graph, node, end, path, shortest)
				if newpath != None:
					shortest = newpath
	return shortest
	


def bfs(graph, src, tgt):
	parents = {src: None}
	queue = deque([src])
	while queue:
		node = queue.popleft()
		for neighbour in graph[node]:
			if neighbour not in parents:
				parents[neighbour] = node
				queue.append(neighbour)
				print(queue)
				if node == tgt:
					break
	path = [tgt]
	while parents[tgt] is not None:
		path.insert(0, parents[tgt])
		tgt = parents[tgt]
	print(path)
g = {"A": ["B", "C"], "B": ["D", "E"], "D": ["F", "G"], "E": ["H"], "C": ["I", "J"], "I": ["K", "L"], "J": ["M"], "F": ["D"], "G": ["D"], "H": ["E"], "K": ["I"], "L": ["I"], "M": ["J"]}
bfs(g, "A", "K")
dfs_shortestpath = dfs(g, "A", "K", [], None)
print(dfs_shortestpath)