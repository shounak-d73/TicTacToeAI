
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

class ComputerPlayerAI(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # square based on minimax algorithm
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, ss, player):
        max_player = self.letter # Human player gets maximizer function to maximize their win, while the computer minimizes its loss
        other_player = 'O' if player == 'X' else 'X'

        if ss.current_winner == other_player: # base case in recursion
            return {'position': None,
                    'score': 1*(ss.num_empty_squares() + 1) if other_player == max_player else -1*(ss.num_empty_squares() + 1)
                    }

        elif not ss.empty_squares():
            return {'position': None, 'score': 0}

        # base case ends

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_moves in ss.available_moves():
            # try a spot and make a move
            ss.make_move(possible_moves, player)
            # recursion to simulate the whole game after every possible move
            sim_score = self.minimax(ss, other_player) 
            # undo the move
            ss.board[possible_moves] = ' '
            ss.current_winner = None
            sim_score['position'] = possible_moves
            # update the dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

