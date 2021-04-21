from player_class import Player
from human_class import Human
from computer_class import Computer


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Computer()
        self.play_mode = " "
        self.game_rounds = 1

    def run_game(self):
        self.game_intro()
        self.play_mode_selection()
        self.play()
        self.display_winner()

    def game_intro(self):
        print("Enter: Rock, Paper, Scissors, Lizard, Spock!\nOnly chance will tell!\n")
        self.player_one.set_name()
        print(f"Welcome {self.player_one.name}")

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
        while self.game_rounds < 3:
            # show gesture options at every round
            print(f"\nROUND {self.game_rounds}!")
            self.display_gesture_options()
            self.player_one.throw_hand()
            self.player_two.computer_hand()
            # compare gestures
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("\nTie!")
                # add a round if there is a tie for the game to go to 3 rounds instead of a best out of two
                self.game_rounds += 1
                self.player_one.score += 1
                self.player_two.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            elif self.player_one.chosen_gesture == "rock":
                if self.player_two.chosen_gesture == 'paper' or self.player_two.chosen_gesture == 'spock':
                    self.player_two.score += 1
                else:
                    self.player_one.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            elif self.player_one.chosen_gesture == "paper":
                if self.player_two.chosen_gesture == 'scissors' or self.player_two.chosen_gesture == 'lizard':
                    self.player_two.score += 1
                else:
                    self.player_one.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            elif self.player_one.chosen_gesture == "scissors":
                if self.player_two.chosen_gesture == 'rock' or self.player_two.chosen_gesture == 'spock':
                    self.player_two.score += 1
                else:
                    self.player_one.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            elif self.player_one.chosen_gesture == "lizard":
                if self.player_two.chosen_gesture == 'rock' or self.player_two.chosen_gesture == 'scissors':
                    self.player_two.score += 1
                else:
                    self.player_one.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            elif self.player_one.chosen_gesture == "spock":
                if self.player_two.chosen_gesture == 'lizard' or self.player_two.chosen_gesture == 'paper':
                    self.player_two.score += 1
                else:
                    self.player_one.score += 1
                print(f"\n{self.player_one.name} : {self.player_one.score}\n{self.player_two.name} : {self.player_two.score}")
            self.game_rounds += 1
            if self.game_rounds == 3 or self.game_rounds >= 3:
                self.display_winner()

    def display_gesture_options(self):
        print(
            f"\nGesture Options:\n0: {self.player_one.gestures[0]}\n1: {self.player_one.gestures[1]}\n2: {self.player_one.gestures[2]}\n3: {self.player_one.gestures[3]}\n4: {self.player_one.gestures[4]}")

    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f"{self.player_one.name} wins!")
        else:
            print(f"{self.player_two.name} wins!")
