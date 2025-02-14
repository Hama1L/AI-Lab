import random

class Environment:
    def __init__(self):
        self.tasks = [random.choice(["Completed", "Failed"]) for _ in range(9)]
    
    def get_percepts(self):
        return self.tasks
    
    def update_task(self, index, status):
        self.tasks[index] = status

class Agent:
    def __init__(self, environment):
        self.environment = environment
    
    def act(self):
        for i, status in enumerate(self.environment.get_percepts()):
            if status == "Failed":
                self.retry(i)
    
    def retry(self, index):
        print(f"Retrying task {index}...")
        self.environment.update_task(index, "Completed")

def run_agent(env, agent):
    print("Initial task status:", env.get_percepts())
    agent.act()
    print("Updated task status:", env.get_percepts())

env = Environment()
agent = Agent(env)
run_agent(env, agent)
