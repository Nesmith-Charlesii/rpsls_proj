import random
from player_class import Player


# inherit from Payer class uses 'Player' as class param and the super()
class Computer(Player):
    def __init__(self):
        super().__init__()

    def computer_gesture(self):
        rand = random.randrange(0, 4)
        computer_choice_gesture = self.gestures[rand]
        print(f"\nAI has chosen to play {computer_choice_gesture}")