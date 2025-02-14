import random

class Environment():
    def __init__(self, components=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], states=['Safe', 'low_risk', 'High_risk']):
        self.system_state = {component: random.choice(states) for component in components}
    
    def display_system_state(self):
        for component, state in self.system_state.items():
            print(f"Component {component}: {state}")
    
    def get_percept(self):
        return self.system_state
    
    def patch_vulnerabilities(self, premium=False):
        print("Patching Vulnerabilities...")
        for component, state in self.system_state.items():
            if state == 'low_risk':
                self.system_state[component] = 'Safe'
                print(f"Component {component}: Patched low risk vulnerability.")
            elif state == 'High_risk' and premium:
                self.system_state[component] = 'Safe'
                print(f"Component {component}: Patched high risk vulnerability using premium service.")
            elif state == 'High_risk':
                print(f"Component {component}: Requires premium service to patch high risk vulnerability.")

class util_agent():
    def __init__(self, premium=False):
        self.premium = premium
    
    def act(self, percept):
        print("Scanning System...")
        for component, state in percept.items():
            if state == 'Safe':
                print(f"Component {component}: Secure.")
            else:
                print(f"Component {component}: Warning! {state} vulnerability detected.")
    
    def patch_vulnerabilities(self, environment):
        environment.patch_vulnerabilities(self.premium)
    
    def final_system_check(self, environment):
        print("Final System Check:")
        environment.display_system_state()

def simulate_security_exercise():
    env = Environment()
    agent = util_agent()
    
    print("Initial System State:")
    env.display_system_state()
    
    agent.act(env.get_percept())
    agent.patch_vulnerabilities(env)
    agent.final_system_check(env)

simulate_security_exercise()
