# library to use the terminal

import os
import msvcrt
import sys
import threading
import time

position_x = 0
position_y = 0
size_x = 0
size_y = 0
fg_color = "\033[38;5;255m"
bg_color = "\033[48;5;0m"

buffer = []
colors = {"black": 0, "blue": 21, "green": 40, "cyan": 44, "red": 160, "purple": 127, "yellow": 226, "white": 250,
          "gray": 244, "light_blue": 33, "light_green": 82, "light_cyan": 45, "light_red": 192, "light_purple": 128,
          "light_yellow": 227, "bright_white": 255}


def set_terminal_size(cols, rows):
    global buffer
    for i in range(rows):
        buffer.append(["{}{} ".format(fg_color, bg_color)] * (cols))
    global size_x
    global size_y
    size_y = rows
    size_x = cols


def get_terminal_size():
    return size_x, size_y


def move_cursor_at(x, y):
    global position_x
    global position_y
    position_y = y
    position_x = x


def in_bounds(x, y):
    return x >= 0 and y >= 0 and x < size_x and y < size_y


def write_at(x, y, text):
    global buffer
    for i in range(len(text)):
        if in_bounds(x + i, y):
            buffer[y][x + i] = fg_color + bg_color + text[i]


def vertical_write_at(x, y, text):
    global buffer
    for i in range(len(text)):
        if in_bounds(x, y + i):
            buffer[y + i][x] = fg_color + bg_color + text[i]


def write(text):
    write_at(position_x, position_y, text)
    move_cursor_at(position_x + len(text), position_y)


def clear_screen():
    os.system('cls')


def set_color(color):
    global fg_color
    fg_color = "\033[38;5;{}m".format(color)


def set_background_color(color):
    global bg_color
    bg_color = "\033[48;5;{}m".format(color)


def reset_color():
    global fg_color
    global bg_color
    fg_color = "\033[38;5;255m"
    bg_color = "\033[48;5;0m"
    print(fg_color + bg_color, end="")


def render():
    global buffer
    set_cursor_position(0, 0)
    lines = []
    for i in range(len(buffer)):
        lines.append("".join(buffer[i]))
    sys.stdout.write("\r".join(lines))
    sys.stdout.flush()


def clear_buffer():
    global buffer
    buffer = []
    for i in range(size_y):
        buffer.append(["{}{} ".format(fg_color, bg_color)] * size_x)


def flush():
    render()
    reset_color()
    clear_buffer()


def get_cursor_position():
    return position_x, position_y


def set_cursor_position(x, y):
    global position_x
    global position_y
    position_x = x
    position_y = y


def _set_non_buffered_cursor(x, y):
    print("\033[{};{}H".format(y, x), end="")


def draw_line(x, y, length, char):
    write_at(x, y, char * length)


def draw_column(x, y, height, char):
    vertical_write_at(x, y, char * height)


def draw_rectangle(x, y, width, height, char):
    draw_line(x, y, width, char)
    draw_line(x, y + height - 1, width, char)
    draw_column(x, y, height, char)
    draw_column(x + width - 1, y, height, char)  # fix the opposite corner of the rectangle


def draw_filled_rectangle(x, y, width, height, char):
    for i in range(height):
        draw_line(x, y + i, width, char)


def compile_buffer():
    global buffer
    last_color = ""
    for i in range(len(buffer)):
        for j in range(len(buffer[i])):
            color_code_lenght, color = _extract_color_from_buffer_cell(j, i)
            if not color:
                pass
            elif color != last_color:
                last_color = color
            else:
                buffer[i][j] = buffer[i][j][color_code_lenght + 1:]


def _extract_color_from_buffer_cell(x, y):
    global buffer
    color = buffer[y][x]
    in_color = False
    last_color_index = 0
    for i in range(len(color)):
        if (color[i] == "\033" and not in_color):
            in_color = True
        elif (color[i] == "m" and in_color):
            in_color = False
            last_color_index = i
    return last_color_index, color[:last_color_index + 1]


#
# Key listener
#


pressed_key = []
__should_stop_key_reader_thread__ = False
__should_stop_key_flusher_thread__ = False


def wait_for_key():
    key = msvcrt.getch()
    if key == b'\xe0':
        key = msvcrt.getch()
        if key == b'H':
            key = b'up'
        elif key == b'P':
            key = b'down'
        elif key == b'M':
            key = b'right'
        elif key == b'K':
            key = b'left'
    return key


def get_key():
    if msvcrt.kbhit():
        return wait_for_key()


def __get_keys_task__():
    global pressed_key
    while True:
        key = get_key()
        if key not in pressed_key:
            pressed_key.append(key)
        if __should_stop_key_reader_thread__:
            break


def flush_keys():
    global pressed_key
    pressed_key = []


def __flush_keys_task__(interval):
    while True:
        flush_keys()
        time.sleep(interval)
        if __should_stop_key_flusher_thread__:
            break


def get_pressed_key():
    global pressed_key
    return pressed_key


def is_key_pressed(key):
    global pressed_key
    return key in pressed_key


__key_reader_thread__ = threading.Thread(target=__get_keys_task__)
__key_flusher_thread__ = threading.Thread(target=__flush_keys_task__, args=(0.1,))


def start_async_key_listener():
    global __key_reader_thread__
    __key_reader_thread__ = threading.Thread(target=__get_keys_task__)
    __key_reader_thread__.start()

def stop_async_key_listener():
    global __should_stop_key_flusher_thread__
    global __should_stop_key_reader_thread__

    if __key_reader_thread__.is_alive():
        __should_stop_key_reader_thread__ = True
        __key_reader_thread__.join()
        __should_stop_key_reader_thread__ = False

    if __key_flusher_thread__.is_alive():
        __should_stop_key_flusher_thread__ = True
        __key_flusher_thread__.join()
        __should_stop_key_flusher_thread__ = False

def set_async_key_listener_interval(interval):
    global __key_flusher_thread__
    global __should_stop_key_flusher_thread__

    if __key_flusher_thread__.is_alive():
        # Stop the thread
        __should_stop_key_flusher_thread__ = True
        __key_flusher_thread__.join()
        __should_stop_key_flusher_thread__ = False

    __key_flusher_thread__ = threading.Thread(target=__flush_keys_task__, args=(interval,))
    __key_flusher_thread__.start()


def _get_key_code_(key):
    if key == "up":
        return b'up'
    elif key == "down":
        return b'down'
    elif key == "right":
        return b'right'
    elif key == "left":
        return b'left'
    elif key == "enter":
        return b'\r'
    elif key == "esc":
        return b'\x1b'
    elif key == "space":
        return b' '
    elif key == "backspace":
        return b'\x08'
    elif key == "tab":
        return b'\t'
    else:
        return key


def is_key_pressed(key):
    global pressed_key
    return _get_key_code_(key) in pressed_key
