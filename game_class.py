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
        print("Rock, Paper, Lizard, Spock! Chance will tell!")

    def play(self):
        pass

    def display_winner(self):
        pass
