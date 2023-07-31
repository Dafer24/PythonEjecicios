class Teory:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        valid_options = {
            "1": "rock",
            "2": "paper",
            "3": "scissors",
            "4": "lizard",
            "5": "spock"
        }

        if self.player1 not in valid_options or self.player2 not in valid_options:
            print("Invalid options. Please enter one of the valid numbers: 1, 2, 3, 4, 5.")
            return

        if self.player1 == self.player2:
            print("It's a tie!")
        elif (self.player1 == "1" and (self.player2 == "3" or self.player2 == "4")) or \
             (self.player1 == "2" and (self.player2 == "1" or self.player2 == "5")) or \
             (self.player1 == "3" and (self.player2 == "2" or self.player2 == "4")) or \
             (self.player1 == "4" and (self.player2 == "2" or self.player2 == "5")) or \
             (self.player1 == "5" and (self.player2 == "1" or self.player2 == "3")):
            print(f"Player 1 ({valid_options[self.player1]}) wins!")
        else:
            print(f"Player 2 ({valid_options[self.player2]}) wins!")

player_1 = input("Player 1, enter your choice (1 - rock, 2 - paper, 3 - scissors, 4 - lizard, 5 - spock): ")
player_2 = input("Player 2, enter your choice (1 - rock, 2 - paper, 3 - scissors, 4 - lizard, 5 - spock): ")

game = Teory(player_1, player_2)
game.play()
