# proxy used to redirect the calls to the right display

use_termilib = False
use_pygame = False

if use_termilib:
    import Display.termilibDisplay as termilibDisplay
elif use_pygame:
    import Display.pygameDisplay as pygameDisplay
else:
    import Display.terminalDisplay as terminalDisplay


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
