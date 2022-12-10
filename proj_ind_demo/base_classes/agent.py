# Define Agent to move in graph
class Agent:
    def __init__(self, speed) -> None:
        self.speed = speed

    def move(self, possible_moves):
        # Agent selects one of the possible moves it can make and goes there
        # Will make choice based on prior info
        pass