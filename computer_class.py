import random
from player_class import Player


# inherit from Payer class uses 'Player' as class param and the super()
class Computer(Player):
    def __init__(self):
        super().__init__()

    def throw_hand(self):
        rand = random.randrange(0, 4)
        self.chosen_gesture = self.gestures[rand]
        print(f"{self.name} has chosen to play {self.chosen_gesture}")
