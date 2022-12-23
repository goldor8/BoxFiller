# proxy used to redirect the calls to the right display

import Display.termilibDisplay as termilibDisplay
import Display.terminalDisplay as terminalDisplay
try:
    import Display.pygameDisplay as pygameDisplay
except ModuleNotFoundError:
    print("pygame is not installed. You can't run the pygame version of this game.")

use_termilib = False
use_pygame = False


def init_display(display_type):  # set the display to use
    global use_termilib, use_pygame
    if display_type == "termilib":
        use_termilib = True
    elif display_type == "pygame":
        use_pygame = True


def show_board(play_grid, blocks):  # show the main information of the game
    if use_termilib:
        termilibDisplay.show_board(play_grid, blocks)
    elif use_pygame:
        pygameDisplay.show_board(play_grid, blocks)
    else:
        terminalDisplay.show_board(play_grid, blocks)


def select_grid_type():  # ask user to select a grid type
    if use_termilib:
        return termilibDisplay.select_grid_type()
    elif use_pygame:
        return pygameDisplay.select_grid_type()
    else:
        return terminalDisplay.select_grid_type()


def select_grid_size():  # ask user to select a grid size
    if use_termilib:
        return termilibDisplay.select_grid_size()
    elif use_pygame:
        return pygameDisplay.select_grid_size()
    else:
        return terminalDisplay.select_grid_size()


def menu():  # show the user a menu and ask to choose play or show rules option
    if use_termilib:
        return termilibDisplay.menu()
    elif use_pygame:
        return pygameDisplay.menu()
    else:
        return terminalDisplay.menu()


def show_rules():  # show rules to the user
    if use_termilib:
        termilibDisplay.show_rules()
    elif use_pygame:
        pygameDisplay.show_rules()
    else:
        terminalDisplay.show_rules()


def get_input_not_parsed(text):  # get input from different display system
    if use_termilib:
        return termilibDisplay.get_input_not_parsed(text)
    elif use_pygame:
        return pygameDisplay.get_input_not_parsed(text)
    else:
        return terminalDisplay.get_input_not_parsed(text)


def select_block(round_blocks):  # ask user to select a block
    if use_termilib:
        return termilibDisplay.select_block(round_blocks)
    elif use_pygame:
        return pygameDisplay.select_block(round_blocks)
    else:
        return terminalDisplay.select_block(round_blocks)


def select_block_position(play_grid, selected_block):  # ask user to select a block position
    if use_termilib:
        return termilibDisplay.select_block_position(play_grid, selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_position(play_grid, selected_block)
    else:
        return terminalDisplay.select_block_position(play_grid, selected_block)


def select_block_rotation(selected_block):  # ask user for a rotation
    if use_termilib:
        return termilibDisplay.select_block_rotation(selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_rotation(selected_block)
    else:
        return terminalDisplay.select_block_rotation(selected_block)


def show_game_over(score):  # show game over screen
    if use_termilib:
        termilibDisplay.show_game_over(score)
    elif use_pygame:
        pygameDisplay.show_game_over(score)
    else:
        terminalDisplay.show_game_over(score)


def select_block_picking_way():
    block_picking_way = 0
    while block_picking_way != 1 and block_picking_way != 2:
        block_picking_way = int(input("choose if you want to play with 3 random blocks or all the blocks : "))
    return block_picking_way
