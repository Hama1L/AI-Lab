class Environment:
    def __init__(self):
         self.grid = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }
    def get_precept(self):
        return self.grid
    def extinguish(self,room):
        self.grid[room]='safe'
        
class FirefightingRobot:
    def __init__(self,environment):
        self.environment=environment
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        self.current_position = 'a'
        
    
    def display_environment(self):
        print("Current Environment Status:")
        grid =self.environment.get_precept()
        for i, room in enumerate(self.path):
            status = "🔥" if grid[room] == 'fire' else "✅"
            print(f"Room {room}: {status}", end='  ')
            if (i + 1) % 3 == 0:
                print('\n')
        print('\n')
    
    def move_and_extinguish(self):
        for room in self.path:
            self.current_position = room
            grid =self.environment.get_precept()
            print(f"Moving to room {room}...")
            if grid[room] == 'fire':
                print(f"Fire detected in room {room}! Extinguishing...")
                self.environment.extinguish(room)
            else:
                print(f"Room {room} is safe.")
            self.display_environment()
        print("All rooms have been checked. Final environment status:")
        self.display_environment()

# Run the simulation
env=Environment()
robot = FirefightingRobot(env)
robot.move_and_extinguish()
