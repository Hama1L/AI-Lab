import heapq
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5, "E": 10},
    "C": {"A": 2, "E": 8},
    "D": {"B": 5, "F": 6},
    "E": {"B": 10, "C": 8, "F": 3},
    "F": {"D": 6, "E": 3, "G": 2},
    "G": {"F": 2},
}
def beam_search(start,goal,beam_width=2):
    beam = [ (0,[start])]
    candidates=[]
    while beam :
        for cost,path in beam:
            current_node = path[-1]
            if current_node == goal :
                return path.reverse()
            for neigbhours,edge_cost in graph[current_node].items():
                new_cost = cost + edge_cost
                new_path = path + [neigbhours]
                candidates.append((new_cost,new_path))
        beam = heapq .nsmallest(beam_width,candidates,key = lambda x : x[0])
                
        
    return False


    