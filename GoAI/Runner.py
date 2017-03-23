#RUNNER

from AllGroups import AllGroups
from SGF import SGFReader
from Board import Board
from Group import Group
from Move import Move
import time
import Rules
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():

    board = Board()
    all_groups = AllGroups()
    player = 'X'

    reader = SGFReader("test.sgf")
    counter = 0
    SFG = False

    while(True):

        time.sleep(.5)
        cls()
        board.print_board()

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

        if not all_groups.move_part_of_any_group(move, board):
            all_groups.add_group(Group([move], player, board))

        all_groups.update(move, board)

        if player == 'X': player = 'O'
        else: player = 'X'
 
main()
