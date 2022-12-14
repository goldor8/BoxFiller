import Display.termilibDisplay as termilibDisplay
import Display.terminalDisplay as terminalDisplay

use_termilib = True


def show_board(play_grid, blocks):
    if use_termilib:
        termilibDisplay.show_board(play_grid, blocks)
    else:
        terminalDisplay.show_board(play_grid, blocks)


def select_grid_type():
    if use_termilib:
        return termilibDisplay.select_grid_type()
    else:
        return terminalDisplay.select_grid_type()


def select_grid_size():
    if use_termilib:
        return termilibDisplay.select_grid_size()
    else:
        return terminalDisplay.select_grid_size()


def menu():
    if use_termilib:
        return termilibDisplay.menu()
    else:
        return terminalDisplay.menu()


def show_rules():
    if use_termilib:
        termilibDisplay.show_rules()
    else:
        terminalDisplay.show_rules()


def get_input(text):
    if use_termilib:
        return termilibDisplay.get_input(text)
    else:
        return terminalDisplay.get_input(text)


def get_input_not_parsed(text):
    if use_termilib:
        return termilibDisplay.get_input_not_parsed(text)
    else:
        return terminalDisplay.get_input_not_parsed(text)
