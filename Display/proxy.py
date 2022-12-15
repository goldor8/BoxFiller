import Display.termilibDisplay as termilibDisplay
import Display.terminalDisplay as terminalDisplay
import Display.pygameDisplay as pygameDisplay

use_termilib = False
use_pygame = True


def show_board(play_grid, blocks):
    if use_termilib:
        termilibDisplay.show_board(play_grid, blocks)
    elif use_pygame:
        pygameDisplay.show_board(play_grid, blocks)
    else:
        terminalDisplay.show_board(play_grid, blocks)


def select_grid_type():
    if use_termilib:
        return termilibDisplay.select_grid_type()
    elif use_pygame:
        return pygameDisplay.select_grid_type()
    else:
        return terminalDisplay.select_grid_type()


def select_grid_size():
    if use_termilib:
        return termilibDisplay.select_grid_size()
    elif use_pygame:
        return pygameDisplay.select_grid_size()
    else:
        return terminalDisplay.select_grid_size()


def menu():
    if use_termilib:
        return termilibDisplay.menu()
    elif use_pygame:
        return pygameDisplay.menu()
    else:
        return terminalDisplay.menu()


def show_rules():
    if use_termilib:
        termilibDisplay.show_rules()
    elif use_pygame:
        pygameDisplay.show_rules()
    else:
        terminalDisplay.show_rules()


def get_input(text):
    if use_termilib:
        return termilibDisplay.get_input(text)
    elif use_pygame:
        return pygameDisplay.get_input(text)
    else:
        return terminalDisplay.get_input(text)


def get_input_not_parsed(text):
    if use_termilib:
        return termilibDisplay.get_input_not_parsed(text)
    elif use_pygame:
        return pygameDisplay.get_input_not_parsed(text)
    else:
        return terminalDisplay.get_input_not_parsed(text)


def select_block(round_blocks):
    if use_termilib:
        return termilibDisplay.select_block(round_blocks)
    elif use_pygame:
        return pygameDisplay.select_block(round_blocks)
    else:
        return terminalDisplay.select_block(round_blocks)


def select_block_position(play_grid, selected_block):
    if use_termilib:
        return termilibDisplay.select_block_position(play_grid, selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_position(play_grid, selected_block)
    else:
        return terminalDisplay.select_block_position(play_grid, selected_block)

def select_block_rotation(selected_block):
    if use_termilib:
        return termilibDisplay.select_block_rotation(selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_rotation(selected_block)
    else:
        return terminalDisplay.select_block_rotation(selected_block)


def show_game_over(score):
    if use_termilib:
        termilibDisplay.show_game_over(score)
    elif use_pygame:
        pygameDisplay.show_game_over(score)
    else:
        terminalDisplay.show_game_over(score)