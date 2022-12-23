"""
Project : BoxFiller
Description : This module is used to redirect the display to the right display system
Author : Brisset Dimitri, Occhiminuti Marius
"""

import Display.termilibDisplay as termilibDisplay
import Display.terminalDisplay as terminalDisplay
try:
    import Display.pygameDisplay as pygameDisplay
except ModuleNotFoundError:
    print("pygame is not installed. You can't run the pygame version of this game.")

use_termilib = False
use_pygame = False


def init_display(display_type: str) -> None:
    """
    set the display to use
    :param display_type: the display type to use ("termilib", "pygame", nothing (terminal))
    :return: None (set the global variable)
    """
    global use_termilib, use_pygame
    if display_type == "termilib":
        use_termilib = True
    elif display_type == "pygame":
        use_pygame = True


def show_board(play_grid: list, blocks: list) -> None:
    """
    show the main information of the game
    :param play_grid: the grid to display
    :param blocks: the blocks to display
    :return: None (only display the grid and the blocks)
    """
    if use_termilib:
        termilibDisplay.show_board(play_grid, blocks)
    elif use_pygame:
        pygameDisplay.show_board(play_grid, blocks)
    else:
        terminalDisplay.show_board(play_grid, blocks)


def select_grid_type() -> int:
    """
    ask user to select a grid type
    :return: the grid type selected (0 = circle, 1 = triangle, 2 = lozenge)
    """
    if use_termilib:
        return termilibDisplay.select_grid_type()
    elif use_pygame:
        return pygameDisplay.select_grid_type()
    else:
        return terminalDisplay.select_grid_type()


def select_grid_size() -> int:
    """
    ask user to select a grid size
    :return: the grid size selected
    """
    if use_termilib:
        return termilibDisplay.select_grid_size()
    elif use_pygame:
        return pygameDisplay.select_grid_size()
    else:
        return terminalDisplay.select_grid_size()


def menu() -> int:
    """
    show the user a menu and ask to choose play or show rules option
    :return: the option selected (0 = play, 1 = show rules)
    """
    if use_termilib:
        return termilibDisplay.menu()
    elif use_pygame:
        return pygameDisplay.menu()
    else:
        return terminalDisplay.menu()


def show_rules() -> None:
    """
    show the rules to the user
    :return: None (only display the rules)
    """
    if use_termilib:
        termilibDisplay.show_rules()
    elif use_pygame:
        pygameDisplay.show_rules()
    else:
        terminalDisplay.show_rules()


def get_input_not_parsed(text: str) -> str:
    """
    get input from different display system
    :param text: the text to display
    :return: the input from the user
    """
    if use_termilib:
        return termilibDisplay.get_input_not_parsed(text)
    elif use_pygame:
        return pygameDisplay.get_input_not_parsed(text)
    else:
        return terminalDisplay.get_input_not_parsed(text)


def select_block(round_blocks: list) -> int:
    """
    ask user to select a block
    :param round_blocks: the blocks to choose from
    :return: the index of block selected
    """
    if use_termilib:
        return termilibDisplay.select_block(round_blocks)
    elif use_pygame:
        return pygameDisplay.select_block(round_blocks)
    else:
        return terminalDisplay.select_block(round_blocks)


def select_block_position(play_grid: list, selected_block: list) -> tuple:
    """
    ask user to select a block position
    :param play_grid: the grid to play on
    :param selected_block: the block to place
    :return: the position selected (x, y)
    """
    if use_termilib:
        return termilibDisplay.select_block_position(play_grid, selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_position(play_grid, selected_block)
    else:
        return terminalDisplay.select_block_position(play_grid, selected_block)


def select_block_rotation(selected_block: list) -> list:
    """
    ask user to select a block rotation
    :param selected_block: the block to rotate
    :return: the rotated block
    """
    if use_termilib:
        return termilibDisplay.select_block_rotation(selected_block)
    elif use_pygame:
        return pygameDisplay.select_block_rotation(selected_block)
    else:
        return terminalDisplay.select_block_rotation(selected_block)


def show_game_over(score: int) -> None:
    """
    show the game over screen
    :param score: the score of the player
    :return: None (only display the game over screen)
    """
    if use_termilib:
        termilibDisplay.show_game_over(score)
    elif use_pygame:
        pygameDisplay.show_game_over(score)
    else:
        terminalDisplay.show_game_over(score)


def select_block_picking_manner() -> int:
    """
    ask user to select a block picking manner
    :return: the block picking manner selected (0 = all block, 1 = 3 random blocks)
    """
    if use_termilib:
        return termilibDisplay.select_block_picking_manner()
    elif use_pygame:
        return pygameDisplay.select_block_picking_manner()
    else:
        return terminalDisplay.select_block_picking_manner()
