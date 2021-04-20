from player_class import Player


# inherit from Payer class uses 'Player' as class param and the super()
class Human(Player):
    def __init__(self):
        super().__init__()