
agent_table = {
    ('Clean', 'A'): 'MoveRight',
    ('Clean', 'B'): 'MoveLeft',
    ('Dirty', 'A'): 'Suck',
    ('Dirty', 'B'): 'Suck'
}


class VacuumCleaner:
    def __init__(self, location='A', room_statuses=None):
        if room_statuses is None:
            room_statuses = {'A': 'Dirty', 'B': 'Dirty'}

        self.location = location
        self.room_statuses = room_statuses

    def percept(self):
        return (self.room_statuses[self.location], self.location)

    def act(self, action):
        if action == 'MoveRight':
            self.location = 'B'

        elif action == 'MoveLeft':
            self.location = 'A'

        elif action == 'Suck':
            self.room_statuses[self.location] = 'Clean'

        elif action == 'NoOp':
            pass

    def get_cleaning_percentage(self):
        total_rooms = len(self.room_statuses)
        clean_rooms = sum(
            1 for status in self.room_statuses.values() if status == 'Clean'
        )

        if total_rooms == 0:
            return 0.0
        return (clean_rooms / total_rooms) * 100

    def get_overall_cleaning_status(self):
        if self.get_cleaning_percentage() == 100:
            return "The entire floor is CLEAN"
        else:
            return "The floor is not yet clean"


def table_driven_agent(percept):
    return agent_table.get(percept, 'NoOp')



if __name__ == "__main__":
    vacuum = VacuumCleaner(
        location='A',
        room_statuses={'A': 'Dirty', 'B': 'Dirty'}
    )

    for step in range(5):
        percept = vacuum.percept()
        action = table_driven_agent(percept)

        print(f"Step {step + 1}")
        print(f"Percept: {percept}")
        print(f"Action: {action}")

        vacuum.act(action)

        print(f"Current Room Status: {vacuum.room_statuses}")
        print(f"Floor cleaned = {vacuum.get_cleaning_percentage():.2f}%")
        print(f"Overall status: {vacuum.get_overall_cleaning_status()}")
        print("-" * 50)
