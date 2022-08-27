from replit import clear
from TicTacToe_art import game_title, bye
from TicTacToe_functions import TicTacToe


def start_game():
    clear()
    print(game_title)
    print("WELCOME TO THE TIC TAC TOE GAME\n")
    new_game = TicTacToe()
    winner_exist = new_game.search_winner()

    def header():
        clear()
        print(game_title)
        print(new_game.error)
        print(new_game.current_game)

    while not new_game.game_over:
        header()
        new_game.next_move()
        winner_exist = new_game.search_winner()
    if winner_exist:
        header()
        if new_game.game_mode == '1' or (new_game.game_mode == '2' and new_game.current_player == new_game.player_1):
            print(f"Congratulations {new_game.current_player} you are the winner!")
        else:
            print(f"I'm sorry {new_game.player_1}, you've been beaten by the PC.")
    else:
        print(f"No one won this time, {new_game.player_1} and {new_game.player_2} are tied.")
    game_continue = input('\n\nDo you want to start another match?\nType "Y" to continue or any '
                          'other key to exit:\t').upper()
    if game_continue == 'Y':
        start_game()
    else:
        print(bye)


start_game()
