import random
def calculate_conflicts(state):
    conflicts=0
    for i in range (len(state)):
        for j in range (1,len(state)):
            if (state[i]==state[j]) or abs(state[i]-state[j])==abs(i-j):
                conflicts +=1
    return conflicts
def get_neighbors(state):
    neighbors= []
    n= len(state)
    for i in range(n):
        for j in range(n):
            if j !=state[i] :
                new_state=list(state)
                new_state[i]=j
                neighbors.append(new_state)
    return neighbors

def hill_climb(n):
    current_state = [random.randint(0,n-1)for _ in range(len(n))]
    current_conflicts =calculate_conflicts(current_state)
    while True :
        neigbhors=get_neighbors(current_state)
        next_state= None
        next_conflicts = current_conflicts
        for neighbor in neigbhors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_conflicts = neighbor_conflicts
                next_state=neighbor
                break 
        if next_conflicts >= current_conflicts:
            break
        current_state = next_state
        current_conflicts = next_conflicts
    return current_state,current_conflicts