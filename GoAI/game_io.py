## Interface and GUI

import os

""" Clears the terminal for multiple os.
"""
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

""" Checks the input the user enters in the terminal.
    Returns false if something is wrong. True if the
    input consists of cordinates to a move.
"""
def check_input(player_input):
    if not ":" in player_input:
        return False
    player_input = player_input.split(":")
    if player_input[0].isdigit() and player_input[0].isdigit():
        for num in range(len(player_input)):
            player_input[num] = int(player_input[num])
            if player_input[num] < 1 or player_input[num] > 19:
                return False
    return player_input