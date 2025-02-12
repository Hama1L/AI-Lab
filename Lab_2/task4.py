import random

class Environment():
    def __init__(self,components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],states = ['Safe', 'low_risk', 'High_risk']):
        self.system_state = {component:random.choice(states) for component in components }  
        
    def display_system_state(self):
        for component, state in self.system_state.items():
            print(f"Component {component}: {state}")
            
    def get_percept(self):
        return self.system_state
    def patch_vulnerabilities(self):
        
        print("Patching Vulnerabilities...")
        for component, state in self.system_state.items():
            if state == 'low_risk':
                self.system_state[component] = 'Safe'
                print(f"Component {component}: Patched low risk vulnerability.")
            elif state == 'High_risk':
                print(f"Component {component}: Requires premium service to patch high risk vulnerability.")
            

class utility_based_agent():
    def __init__(self,premium=False):
       self.service = premium
       
    def act(self,percept):
        system_state = percept.get_percept()
        for component,state in system_state.items():
            
        
        
   
   

    

    

def simulate_security_exercise():
    agent = utility_based_agent() 
    agent.scan_system()  
    agent.patch_vulnerabilities()  
    agent.final_system_check()  

simulate_security_exercise()