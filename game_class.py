from player_class import Player
from human_class import Human
from computer_class import Computer

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Computer()
        self.play_mode = " "
        self.game_rounds = 3

    def run_game(self):
        self.game_intro()
        self.play_mode_selection()
        self.play()
        self.display_winner()

    def game_intro(self):
        print("Enter: Rock, Paper, Scissors, Lizard, Spock!\nOnly chance will tell!\n")
        self.player_one.set_name()

    # CREATE A WHILE LOOP TO RE-PROMPT FOR VALIDITY
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
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.display_gesture_options()
            self.player_one.throw_hand()
            self.player_two.computer_hand()
            if self.player_one.throw_hand() == 'rock':
                pass
            if self.player_one.throw_hand() == 'paper':
                pass
            if self.player_one.throw_hand() == 'scissors':
                pass
            if self.player_one.throw_hand() == 'lizard':
                pass
            if self.player_one.throw_hand() == 'spock':
                pass
        pass

    def display_gesture_options(self):
        print(
            f"\nGesture Options:\n0: {self.player_one.gestures[0]}\n1: {self.player_one.gestures[1]}\n2: {self.player_one.gestures[2]}\n3: {self.player_one.gestures[3]}\n4: {self.player_one.gestures[4]}")

    def display_winner(self):
        pass
