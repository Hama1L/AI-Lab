import random


class DataCenter:
    def __init__(self, states=["Underloaded", "Balanced", "Overloaded"]):
        self.servers = [states[random.randint(0, 2)] for _ in range(5)]


    def get_percept(self):
        return self.servers


    def move_task(self, from_server, to_server):
        print(f"Moving task from Server {from_server} to Server {to_server}.")
        self.servers[from_server] = "Balanced"
        self.servers[to_server] = "Balanced"


    def print_state(self):
        print("System Servers Load State:", self.servers)




class LoadBalancerAgent:
    def __init__(self):
        self.arr = list()  


    def act(self, percept):
        overloaded = []
        underloaded = []
       
        for i in range(len(percept)):
            if percept[i] == "Overloaded":
                overloaded.append(i)
            elif percept[i] == "Underloaded":
                underloaded.append(i)
       
        for over in overloaded:
            if underloaded:
                under = underloaded.pop()  
                print(f"Warning: Server {over} is overloaded; moving tasks to Server {under}.")
                self.arr.append((over, under))  
       
        return self.arr




def run_load_balancer(agent, datacenter):
    percept = datacenter.get_percept()
    print("Initial System State:")
    datacenter.print_state()
   
    actions = agent.act(percept)
   
    print("\nBalancing the Load:")
    for action in actions:
        datacenter.move_task(action[0], action[1])  
   
    print("\nLoad Balancing Complete:")
    datacenter.print_state()




datacenter = DataCenter()
agent = LoadBalancerAgent()
run_load_balancer(agent, datacenter)
