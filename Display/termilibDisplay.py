import time

from Display import termilib
from main import parse_essential_commands


def show_board(play_grid, blocks):
    x_pos = 5
    y_pos = 2
    termilib.set_background_color(termilib.colors["bright_white"])
    termilib.draw_column(x_pos, y_pos, len(play_grid) + 2, " ")
    termilib.draw_column(x_pos + 1 + len(play_grid[0]) * 2 + 3, y_pos, len(play_grid) + 2, " ")
    termilib.draw_rectangle(x_pos + 1, y_pos, len(play_grid[0]) * 2 + 3, len(play_grid) + 2, " ")
    termilib.set_background_color(termilib.colors["black"])
    for y in range(len(play_grid)):
        for x in range(len(play_grid[y])):
            termilib.set_cursor_position(x * 2 + y_pos + 5, y + 3)
            if play_grid[y][x] == 1:
                termilib.write(" -")
            elif play_grid[y][x] == 2:
                termilib.write(" #")

    termilib.compile_buffer()
    termilib.flush()


def select_grid_type():
    grid_type = 0
    while True:
        draw_selected_grid_type(grid_type)
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


def draw_selected_grid_type(grid_type):
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
                return 11
            elif grid_size == 1:
                return 17
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


def get_input(text):
    str = get_input_not_parsed(text)
    if parse_essential_commands(str):
        return get_input(text)
    return str
