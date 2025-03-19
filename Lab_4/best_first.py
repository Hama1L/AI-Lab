import queue
graph = {
'S': [('A', 3), ('B', 6), ('C', 5)],
'A': [('D', 9), ('E', 8)],
'B': [('F', 12),('G', 14)],
'C': [('H', 7)],
'H': [('I', 5),('J', 6)],
'I': [('K', 1),('L', 10), ('M', 2)],
'D': [],'E': [],
'F': [],'G': [],
'J': [],'K': [],
'L': [],'M': []
}
def bfs(graph,start,goal) : 
    visited=set()
    pq=queue.PriorityQueue()
    pq.put((0,start))
    parent={}
    while not pq.empty():
        cost,node=pq.get()
        if node not in visited:
            visited.add(node)
            if node == goal :
                path = []
                for curr in parent:
                    path.append(curr)
                    curr=parent[curr]
                return f"Goal reached {node} {visited} {parent}"
            for neighbor,weight in graph[node]:
                if neighbor not in visited:
                    pq.put((weight,neighbor))
                    parent[neighbor]=node
    return f"Goal not reachable"
print(bfs(graph,'S','G'))