from player_class import Player


class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.play_mode = " "
        self.game_rounds = 3

    def run_game(self):
        self.game_intro()
        self.play_mode_selection()
        self.play()
        self.display_winner()

    def game_intro(self):
        print("Enter: Rock, Paper, Scissors, Lizard, Spock!\nOnly chance will tell!\n")
        user_name = input("Hello new player! Please, enter your name:  ")
        self.player_one.name = user_name

    def play_mode_selection(self):
        mode = input("\nEnter 1 : single player\nEnter 2 : multiplayer\n\tChoose player mode:  ")
        if mode == '1':
            mode = 'SINGLE PLAYER'
        elif mode == '2':
            mode = 'MULTIPLAYER'
        else:
            print("\nPlease enter either 1 or 2 !")
            mode = input("\nEnter 1 : single player\nEnter 2 : multiplayer\n\tChoose player mode:  ")
        self.play_mode = mode
        print(f"\n\t{self.play_mode} selected")

    def play(self):
        self.display_gesture_options()
        pass

    def display_gesture_options(self):
        print(f"\nGesture Options:\n0: {self.player_one.gestures[0]}\n1: {self.player_one.gestures[1]}\n2: {self.player_one.gestures[2]}\n3: {self.player_one.gestures[3]}\n4: {self.player_one.gestures[4]}")
        user_choice = input("\nChoose your hand! : ")
        choice_index = int(user_choice)
        self.player_one.chosen_gesture = self.player_one.gestures[choice_index]
        print(f"{self.player_one.name} has chosen {self.player_one.chosen_gesture} as their hand")

    def display_winner(self):
        pass
