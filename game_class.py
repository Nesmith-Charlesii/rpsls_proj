from player_class import Player


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.game_intro()
        self.play()
        self.display_winner()

    def game_intro(self):
        print("Enter: Rock, Paper, Scissors, Lizard, Spock!\nOnly chance will tell!")

    def play(self):
        self.display_gesture_options()
        pass

    def display_gesture_options(self):
        user_name = input("Hello new player! Please, enter your name: ")
        self.player_one.name = user_name
        print(f"Gesture Options:\n0: {self.player_one.gestures[0]}\n1: {self.player_one.gestures[1]}\n2: {self.player_one.gestures[2]}\n3: {self.player_one.gestures[3]}\n4: {self.player_one.gestures[4]}")
        user_choice = input("Choose your hand!: ")
        choice_index = int(user_choice)
        self.player_one.chosen_gesture = self.player_one.gestures[choice_index]
        print(f"{self.player_one.name} has chosen {self.player_one.chosen_gesture} as their hand")

    def display_winner(self):
        pass
