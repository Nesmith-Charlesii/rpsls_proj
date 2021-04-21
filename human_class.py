from player_class import Player


# inherit from Payer class uses 'Player' as class param and the super()
class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        user_name = input("Hello new player! Please, enter your name:  ")
        while not user_name.isalpha():
            print("\nPlayer names must be letters only")
            user_name = input("Hello new player! Please, enter your name:  ")
        else:
            self.name = user_name

    def throw_hand(self):
        user_choice = input("\nChoose your hand! : ")
        # cast string input return to an integer
        # choice_index = int(user_choice)
        # list of integers for each index in the gesture list
        index_array = [0, 1, 2, 3, 4]
        while True:
            if user_choice.isnumeric():
                choice_index = int(user_choice)
                if index_array.__contains__(choice_index):
                    self.chosen_gesture = self.gestures[choice_index]
                    print(f"\n{self.name} has chosen to play {self.chosen_gesture}")
                    break
                else:
                    print("\nPlease choose from the list of gesture options")
                    user_choice = input("\nChoose your hand! : ")
            else :
                print("\nPlease choose from the list of gesture options")
                user_choice = input("\nChoose your hand! : ")
        # user_choice = input("\nChoose your hand! : ")
        # choice_index = int(user_choice)
        # while choice_index != :
        #     print("\nPlease choose from the list of gesture options")
        #     user_choice = input("\nChoose your hand! : ")
        #     choice_index = int(user_choice)
        # else:
        #     # choice_index = int(user_choice)
        #     self.chosen_gesture = self.gestures[choice_index]
        #     print(f"\n{self.name} has chosen to play {self.chosen_gesture}")
