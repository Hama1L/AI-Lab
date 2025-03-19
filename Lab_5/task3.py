import random 
import math
cities = [
    (0, 0), (1, 3), (2, 5), (5, 4), (6, 8),
    (8, 2), (9, 7), (3, 1), (4, 9), (7, 6)
]
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def fitness(route):
    total_distance = 0
    for i in range(len(route)):
        city1=cities[i]
        city2=cities[(i+1)%len(route)]
        distance_btw = distance(city1,city2)
        total_distance+=distance_btw
    return 1/total_distance

def generate_population(size):
    population=[]
    n= len(route)
    for i in range(size):
        route=random.sample(range(n),n)
        population.append(route)
    return population

def select_parents(population,fitness_values):
    parent1,parent2=random.choices(zip(population,fitness_values),weights=fitness_values,k=2)
    return parent1,parent2

def crossover(parent1,parent2):
    size = len(parent1)
    child= [-1]*size
    start,end=sorted(random.sample(len(parent1),2))
    child[start:end]=parent1[start:end]
    ptr = end
    for city in parent2:
        if city not in child:
            if ptr >= end:
                ptr = 0
            child[ptr]=city
            ptr+=1
    return child

def mutate(route):
    if random.random()<0.2:
        idx,idy=random.sample(len(route),2)
        route[idx],route[idy]=route[idy],route[idx]
    return route

def gen_algo():
    population = generate_population(20)
    
    