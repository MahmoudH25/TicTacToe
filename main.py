import time
from game import TicTacToe
from player import HumanPlayer, ComputerPlayer


def play(game, player_x, player_y, print_game=True):
    if print_game:
        TicTacToe.print_board_nums()

    letter = 'X'
    while game.has_empty_squares():
        square = player_x.get_move(
            game) if letter == "X" else player_y.get_move(game)

        # check if the move is available
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print()

            if game.current_winner != None:
                if print_game:
                    print(f"{letter} wins!!!")
                return letter  # end the loop and exit the game

            letter = "O" if letter == "X" else "X"
            time.sleep(1)  # delay one second between each turn
    # the loop finished and it's a tie.
    if print_game:
        print("It's a tie!!!")


if __name__ == "__main__":
    game = TicTacToe()
    player1 = HumanPlayer('X')
    player2 = ComputerPlayer('O')
    play(game, player1, player2, True)
