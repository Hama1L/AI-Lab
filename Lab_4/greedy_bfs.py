import heapq
def greedy_bfs(graph,start,end,heuristics):
    visited=set()
    open_list = []
    heapq.heappush(open_list,(heuristics[start],start))
    while open_list:
        _,current_node = heapq.heappop(open_list)
        if current_node==end:
            return True
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(open_list,(heuristics[neighbor],neighbor))
    return False

def A_star(graph,start,end,heuristics):
    visited =set()
    open_list=[]
    heapq.heappush(open_list,(0+heuristics[start],0,start))
    g=0
    while open_list:
        _,node_cost,curr_node=heapq.heappop(open_list)
        if curr_node==end:
            return True
        visited.add(curr_node)
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                g+=1
                heapq.heappush(open_list,(g+heuristics[neighbor],g,neighbor))
    return False