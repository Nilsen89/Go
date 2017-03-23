#RUNNER

from allGroups import AllGroups
from sfg import SGFReader
from board import Board
from move import Move
import time
import rules
import testing
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():

    board = Board()
    all_groups = AllGroups()
    player = 'X'

    reader = SGFReader("test.sgf")
    counter = 0
    SFG = True

    while(True):

        time.sleep(.5)
        #cls()

        #print(len(all_groups.groups))
        #for group in all_groups.groups:
        #    print(group.group)

        if SFG:
            move = Move(reader.moves[counter][0], reader.moves[counter][1], player)
            print(move)
            counter = counter + 1
        else: 
            print("PLAYER MOVE: " + player)
            player_input = input("Enter move ex. 4:4: ")
            player_input = Rules.check_input(player_input)
            if not player_input:
                print("False move")
                continue

            move = Move(player_input[0]-1, player_input[1]-1, player)

        if not board.add_move(move):
            continue

        all_groups.move_part_of_any_group(move, board)

        #Do not think this is needed!
        #all_groups.update(move, board)

        if player == 'X': player = 'O'
        else: player = 'X'

        #Testing
        #Testing.set_group_numbers(board, all_groups, True)
        #if move == Move(4,3, 'X'):
        #        Testing.print_group_to_move(board, all_groups, move)
        #        break

        board.print_board()

main()
