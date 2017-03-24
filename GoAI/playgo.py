#RUNNER

from all_groups import AllGroups
from sfg import SGFReader
from player import Player
from board import Board
from move import Move
import game_io
import sys
import time
import rules
import testing

""" Get the next SGF move
"""
def get_sgf_move(reader, move_counter, turn):
    return Move(reader.moves[move_counter][0], reader.moves[move_counter][1], turn.player)

""" Get next player move
"""
def get_player_move(turn):
    print("PLAYER MOVE: " + str(turn))
    player_input = input("Enter move ex. 4:4: ")
    player_input = game_io.check_input(player_input)
    if not player_input:
        print("False move")
        return get_player_move()
    return Move(player_input[0]-1, player_input[1]-1, turn.player)

def main():

    board = Board()
    all_groups = AllGroups()

    player_one = Player('X')
    player_two = Player('O')

    turn = player_one

    reader = SGFReader("test.sgf")
    move_counter = 0
    SGF = True

    while(True):

        if SGF: move = get_sgf_move(reader, move_counter, turn)
        else: move = get_player_move(turn)

        if rules.is_legal_pre_move(board, move): board.add_move(move)
        else: continue
        
        all_groups.move_part_of_any_group(move, board, turn.player)

        if turn.player == player_one.player: turn = player_two
        else: turn = player_one

        #Testing
        testing.set_group_numbers(board, all_groups, False)

        game_io.clear()
        board.print_board()
        time.sleep(.5)

        move_counter = move_counter + 1

main()