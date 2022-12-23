"""
Project : BoxFiller
Description : Display functions when using termilib
Author : Brisset Dimitri
"""

from Display import termilib
from Display.viewBufferUtil import *


def show_board(play_grid, blocks):
    grid_view = []
    x_pos = 5
    y_pos = 2
    clear_view(grid_view)

    # Add letter on top of each column
    termilib.set_cursor_position(x_pos, y_pos)
    first_line = "    "
    for i in range(len(play_grid[0])):
        first_line += chr(ord('a') + i) + "  "
    termilib.write(first_line)

    # Add fancy top border
    termilib.set_cursor_position(x_pos, y_pos + 1)
    top_border = "  ╔"
    for i in range(len(play_grid[0])):
        top_border += "═══"
    top_border += "╗"
    termilib.write(top_border)

    # Draw line Add letter for each line and add fancy border
    for y in range(len(play_grid)):
        termilib.set_cursor_position(x_pos, y_pos + 2 + y)
        line = chr(ord('A') + y) + " ║"  # Add letter for each line and fancy border
        for x in range(len(play_grid[y])):  # Draw each cell
            if play_grid[y][x] == 1:
                line += " . "
            elif play_grid[y][x] == 2:
                line += " ■ "
            elif play_grid[y][x] == 0:
                line += "   "
        line += "║"  # Add fancy border
        termilib.write(line)

    # Add fancy bottom border$
    termilib.set_cursor_position(x_pos, y_pos + 2 + len(play_grid))
    bottom_border = "  ╚"
    for i in range(len(play_grid[0])):
        bottom_border += "═══"
    bottom_border += "╝"
    termilib.write(bottom_border)

    termilib.compile_buffer()
    termilib.flush()


def select_grid_type():
    grid_type = 0
    while True:
        draw_select_grid_type(grid_type)
        if termilib.is_key_pressed("left"):
            grid_type -= 1
        elif termilib.is_key_pressed("right"):
            grid_type += 1
        elif termilib.is_key_pressed("enter"):
            termilib.flush_keys()
            return grid_type
        if grid_type < 0:
            grid_type = 2
        elif grid_type > 2:
            grid_type = 0
        termilib.flush_keys()


def draw_select_grid_type(grid_type):
    termilib.set_cursor_position(40, 3)
    termilib.write("Selected grid type: ")

    termilib.set_cursor_position(30, 5)
    if grid_type == 0:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Circle")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.set_cursor_position(60, 5)
    if grid_type == 1:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Triangle")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.set_cursor_position(90, 5)
    if grid_type == 2:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Lozenge")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.compile_buffer()
    termilib.flush()


def select_grid_size():
    grid_size = 0
    while True:
        draw_selected_grid_size(grid_size)
        if termilib.is_key_pressed("left"):
            grid_size -= 1
        elif termilib.is_key_pressed("right"):
            grid_size += 1
        elif termilib.is_key_pressed("enter"):
            termilib.flush_keys()
            if grid_size == 0:
                return 21
            elif grid_size == 1:
                return 23
            elif grid_size == 2:
                return 25
        if grid_size < 0:
            grid_size = 2
        elif grid_size > 2:
            grid_size = 0
        termilib.flush_keys()


def draw_selected_grid_size(grid_size):
    termilib.set_cursor_position(40, 3)
    termilib.write("Selected grid size: ")

    termilib.set_cursor_position(30, 5)
    if grid_size == 0:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Small")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.set_cursor_position(60, 5)
    if grid_size == 1:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Medium")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.set_cursor_position(90, 5)
    if grid_size == 2:
        termilib.set_background_color(termilib.colors["bright_white"])
        termilib.set_color(termilib.colors["black"])
    termilib.write("Large")
    termilib.set_background_color(termilib.colors["black"])
    termilib.set_color(termilib.colors["bright_white"])

    termilib.compile_buffer()
    termilib.flush()


def menu():
    termilib.set_terminal_size(150, 40)
    termilib.start_async_key_listener()
    selection = 0
    while True:
        draw_menu(selection)
        if termilib.is_key_pressed("up"):
            selection -= 1
        elif termilib.is_key_pressed("down"):
            selection += 1
        elif termilib.is_key_pressed("enter"):
            termilib.flush_keys()
            return selection
        if selection < 0:
            selection = 1
        elif selection > 1:
            selection = 0
        termilib.flush_keys()


def draw_menu(selectedChoice):
    termilib.set_cursor_position(2, 0)
    termilib.write("Tetris")
    termilib.set_cursor_position(2, 1)
    termilib.write("Play")
    termilib.set_cursor_position(2, 2)
    termilib.write("Rules")
    termilib.set_cursor_position(0, selectedChoice + 1)
    termilib.write(">")
    termilib.set_cursor_position(10, selectedChoice + 1)
    termilib.write("<")
    termilib.compile_buffer()
    termilib.flush()


def show_rules():
    # todo
    return


def get_input_not_parsed(text):
    termilib.stop_async_key_listener()
    input_text = input(text)
    termilib.start_async_key_listener()
    return input_text
