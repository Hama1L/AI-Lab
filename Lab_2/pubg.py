import random
class Environment:
 
  def __init__(self,states=["Idle","Under_Attack","Enemies_Ahead"]):
    self.state = states[random.randint(0,2)]
    self.ammo=30
    self.pos=(5,3)


  def get_percept(self):
    return self.state , self.ammo ,self.pos


  def mov_pos(self):
    self.pos[random.randint(0,1)]+=1
    print("Bot Moved")
  def fire(self):
    self.ammo -=1
   
  def reload(self):
    self.ammo=30
    print("Reloaded")
 
class Agent:
  def __init__(self):
    pass
  def act(self,percept):
    if percept=="Idle":
      return "Roam Ideally"
    elif percept == "Under_Attack":
      return "Run"
    else :
      return "Fire"




def run_agent(agent,environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    if action == "Roam Ideally" :
      environment.mov_pos()
    elif action == "Run" :
      while action != "Under_Attack":
        environment.mov_pos()
        percept = environment.get_percept()
        action = agent.act(percept)
       
    else :
      if environment.ammo == 0:
        environment.reload
      else :
        environment.fire()
    print(f"Bot State , Ammo and Position : {percept} action : {action} ")


environment=Environment()
agent=Agent()
run_agent(agent,environment)
