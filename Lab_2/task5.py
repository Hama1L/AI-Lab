import random

class Environment():
    def __init__(self):
        self.locations = {
            'Storage': 'Medicine storage area',
            'Room1': 'Patient Room 1',
            'Room2': 'Patient Room 2',
            'Room3': 'Patient Room 3',
            'NurseStation': 'Nurse station'
        }
        self.patient_schedules = {
            'Room1': {'medicine': 'Painkiller', 'time': '09:00 AM'},
            'Room2': {'medicine': 'Antibiotic', 'time': '10:00 AM'},
            'Room3': {'medicine': 'Vitamins', 'time': '11:00 AM'}
        }
        self.staff_availability = True
    
    def get_percepts(self):
        return self.patient_schedules, self.staff_availability
    
    def alert_staff(self):
        print("Alerting nurses/doctors for assistance...")

class Agent():
    def __init__(self, environment):
        self.environment = environment
        self.current_location = 'Storage'
    
    def move_to(self, location):
        print(f"Moving to {location}...")
        self.current_location = location
    
    def pick_up_medicine(self, medicine):
        print(f"Picking up {medicine} from storage...")
    
    def scan_patient_id(self, room):
        print(f"Scanning patient ID in {room}...")
        return True  
    
    def deliver_medicine(self, room, medicine):
        if self.scan_patient_id(room):
            print(f"Delivering {medicine} to {room}...")
        else:
            print(f"Patient ID verification failed in {room}. Alerting staff...")
            self.environment.alert_staff()
    
    def act(self):
        schedules, staff_available = self.environment.get_percepts()
        for room, details in schedules.items():
            self.move_to('Storage')
            self.pick_up_medicine(details['medicine'])
            self.move_to(room)
            self.deliver_medicine(room, details['medicine'])
            if not staff_available:
                self.environment.alert_staff()

def run_agent():
    env = Environment()
    agent =Agent(env)
    print("Starting hospital delivery robot simulation...")
    agent.act()
    print("Simulation complete.")

run_agent()
