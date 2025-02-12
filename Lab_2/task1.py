import random
class Environment:
 
  def __init__(self,states=["Safe","Vulnerable"]):
    self.components = [states[random.randint(0,1)] for i in range (9)]
   


  def get_percept(self):
    return self.components


  def change_state(self,pos):
    self.components[pos]="Safe"
 
  def print_state(self):
    print(self.components)


 
class Agent:
  def __init__(self):
    self.arr=list()
  def act(self,percept):
    for i in range(len(percept)):
      if percept[i]=="Safe":
        print(f"Component {i} Safe")
      else :
        self.arr.append(i)
        print( f"Warning component{i} is critical ;added to the list for patching")
    return self.arr
     
   
def run_agent(agent,environment):
    percept = environment.get_percept()
    print("System Components ", percept)
    action = agent.act(percept)
   
    print("Patching Vulnerabilities")
    for i in action:
      environment.change_state(i)
    print("Scan Complete  : ")
    print("System Components after patch ", percept)


environment=Environment()
agent=Agent()
run_agent(agent,environment)