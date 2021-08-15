
import math
import random

class Player:
    def __init__(self, letter):
        # x or o letter
        self.letter = letter

    def get_move(self, game):  
        # getting players their next move
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # random valid spot for the computer 
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # else, to come out of loop
            except ValueError:
                print("Invalid move!! Try Again!")

        return val



