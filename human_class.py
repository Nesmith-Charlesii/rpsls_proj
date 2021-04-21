from player_class import Player


# inherit from Payer class uses 'Player' as class param and the super()
class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        user_name = input("Hello new player! Please, enter your name:  ")
        self.name = user_name

    def throw_hand(self):
        user_choice = input("\nChoose your hand! : ")
        choice_index = int(user_choice)
        self.chosen_gesture = self.gestures[choice_index]
        print(f"\n{self.name} has chosen to play {self.chosen_gesture}")
