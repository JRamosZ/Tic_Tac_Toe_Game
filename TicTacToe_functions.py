import random
from TicTacToe_art import game_base

# These are the positions to put the marks according to the TicTacToe_art. Do not change.
LIST_POSITIONS = [16, 20, 24, 68, 72, 76, 120, 124, 128]
WINNING_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


class TicTacToe:
    def __init__(self):
        self.player_1 = input("Hello, what's your name?\t")
        self.player_2 = 'Automated_ECU'
        self.error = ''
        self.game_mode = None
        self.game_mode_selection()
        if self.game_mode == '1':
            self.player_2 = input('What"s the name of the second player?\t')
        self.game_over = False
        self.current_game = game_base
        self.current_game_list = list(self.current_game)
        self.turn = 1
        self.current_player = self.player_1
        self.current_player_mark = 'X'

    def game_mode_selection(self):
        """Function to catch the desired game mode. P vs P | P vs CPU"""
        mode = input(f'Hello {self.player_1}, type 1 to play against other user or 2 to play with the PC:\t')
        if mode != '1' and mode != '2':
            self.game_mode_selection()
        else:
            self.game_mode = mode

    def get_current_player(self):
        """Function to determiate which player is currently playing"""
        if self.turn % 2 == 1:
            self.current_player = self.player_1
            self.current_player_mark = 'X'
        else:
            self.current_player = self.player_2
            self.current_player_mark = 'O'

    def next_move(self):
        """This function will manage both the real players and automated hits"""
        if not self.hits_available():
            self.game_over = True
            return
        self.get_current_player()
        if self.game_mode == '1' or self.current_player == self.player_1:
            position = input(f"Hey {self.current_player} it's your turn, where do you want to hit?\nUse the template "
                             f"on the left for reference\t")
            try:
                position = int(position)
            except ValueError:
                self.error = "Thats not a valid position, try again"
            else:
                if 1 <= position <= 9:
                    if self.current_game_list[LIST_POSITIONS[position-1]] == ' ':
                        self.current_game_list[LIST_POSITIONS[position-1]] = self.current_player_mark
                        self.current_game = ''.join(self.current_game_list)
                        self.turn += 1
                        self.error = ''
                    else:
                        self.error = "That position is already taken, try another"
                else:
                    self.error = "Thats not a valid position, try again"
        elif self.game_mode == '2':
            # The computer will first search for a place to win and then for a place to not lose
            if self.find_strategic_place('O') or self.find_strategic_place('X'):
                return
            # In case there are not strategic places to hit, it will randomly select a spot
            else:
                empty_spaces = [pos for pos in LIST_POSITIONS if self.current_game_list[pos] == ' ']
                self.current_game_list[random.choice(empty_spaces)] = self.current_player_mark
                self.current_game = ''.join(self.current_game_list)
                self.turn += 1

    def search_winner(self):
        """This function will look for a combination of 3 equals marks to see if there is a winner"""
        for combination in WINNING_COMBINATIONS:
            if self.current_game_list[LIST_POSITIONS[combination[0]-1]] ==\
                    self.current_game_list[LIST_POSITIONS[combination[1]-1]] ==\
                    self.current_game_list[LIST_POSITIONS[combination[2]-1]] != ' ':
                self.game_over = True
                return True

    def hits_available(self):
        """This function will look for empty places to keep on playing"""
        for pos in LIST_POSITIONS:
            if self.current_game_list[pos] == ' ':
                return True
        return False

    def find_strategic_place(self, char):
        """This function will look for the ideal place to hit to win or avoid losing the match"""
        for combination in WINNING_COMBINATIONS:
            chars_list = [self.current_game_list[LIST_POSITIONS[index-1]] for index in combination]
            if chars_list.count(char) == 2 and chars_list.count(' ') == 1:
                winner_combination_index = WINNING_COMBINATIONS.index(combination)
                winner_index = chars_list.index(' ')
                position_to_hit = WINNING_COMBINATIONS[winner_combination_index][winner_index]
                self.current_game_list[LIST_POSITIONS[position_to_hit-1]] = self.current_player_mark
                self.current_game = ''.join(self.current_game_list)
                self.turn += 1
                return True
        return False
