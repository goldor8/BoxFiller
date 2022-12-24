import os
import sys
try:
    import msvcrt
    import_mode = "win"
except:
    import termios, tty
    import_mode = "lin"
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


def set_terminal_size(cols: int, rows: int) -> None:
    """
    Set the terminal size
    :param cols: number of columns
    :param rows: number of rows
    :return: None
    """
    global buffer
    for i in range(rows):
        buffer.append(["{}{} ".format(fg_color, bg_color)] * (cols))
    if import_mode == "win":
        os.system('mode con: cols={} lines={}'.format(cols, rows))
    global size_x
    global size_y
    size_y = rows
    size_x = cols


def get_terminal_size() -> tuple:
    """
    Get the terminal size
    :return: (columns, rows)
    """
    return size_x, size_y


def move_cursor_at(x: int, y: int) -> None:
    """
    Move the cursor at the given position
    :param x: x position
    :param y: y position
    :return: None
    """
    global position_x
    global position_y
    position_y = y
    position_x = x


def in_bounds(x: int, y: int) -> bool:
    """
    Check if the given position is in the terminal bounds
    :param x: x position
    :param y: y position
    :return: True if the position is in the terminal bounds, False otherwise
    """
    return x >= 0 and y >= 0 and x < size_x and y < size_y


def write_at(x: int, y: int, text: str) -> None:
    """
    Write the given text at the given position
    :param x: x position
    :param y: y position
    :param text: text to write
    :return: None
    """
    global buffer
    for i in range(len(text)):
        if in_bounds(x + i, y):
            buffer[y][x + i] = fg_color + bg_color + text[i]


def write_at_with_increment_gradient(x, y, text, color):
    global buffer
    for i in range(len(text)):
        set_color(color + i)
        write_at(x + i, y, text[i])


def vertical_write_at(x: int, y: int, text: str) -> None:
    """
    Write the given text vertically at the given position
    :param x: x position
    :param y: y position
    :param text: text to write
    :return: None
    """
    global buffer
    for i in range(len(text)):
        if in_bounds(x, y + i):
            buffer[y + i][x] = fg_color + bg_color + text[i]


def write(text: str) -> None:
    """
    Write the given text at the current cursor position
    :param text: text to write
    :return: None
    """
    write_at(position_x, position_y, text)


def clear_screen() -> None:
    """
    Clear the terminal screen
    :return: None
    """
    if import_mode == "win":
        os.system('cls')
    else:
        os.system('clear')


def set_color(color: int) -> None:
    """
    Set the foreground color
    :param color: color to set
    :return: None
    """
    global fg_color
    fg_color = "\033[38;5;{}m".format(color)


def set_rgb_color(r, g, b):
    global fg_color
    fg_color = "\033[38;2;{};{};{}m".format(r, g, b)


def set_background_color(color: int) -> None:
    """
    Set the background color
    :param color: color to set
    :return: None
    """
    global bg_color
    bg_color = "\033[48;5;{}m".format(color)


def set_rgb_background_color(r, g, b):
    global bg_color
    bg_color = "\033[48;2;{};{};{}m".format(r, g, b)


def reset_color() -> None:
    """
    Reset the color (white foreground and black background)
    :return: None
    """
    global fg_color
    global bg_color
    fg_color = "\033[38;5;255m"
    bg_color = "\033[48;5;0m"
    print(fg_color+bg_color, end="")


def render() -> None:
    """
    Render the buffer to the terminal
    :return: None
    """
    global buffer
    set_cursor_position(0, 0)
    _set_non_buffered_cursor(0, 0)
    lines = []
    for i in range(len(buffer)):
        lines.append("".join(buffer[i]))
    print("\n".join(lines), end="")


def clear_buffer() -> None:
    """
    Clear the buffer
    :return: None
    """
    global buffer
    buffer = []
    for i in range(size_y):
        buffer.append(["{}{} ".format(fg_color, bg_color)] * size_x)


def flush() -> None:
    """
    Render the buffer to the terminal, clear the buffer and reset the color and the cursor position
    :return: None
    """
    render()
    reset_color()
    clear_buffer()


def get_cursor_position() -> tuple:
    """
    Get the cursor position
    :return: (x, y)
    """
    return position_x, position_y


def set_cursor_position(x: int, y: int) -> None:
    """
    Set the cursor position in the buffer
    :param x: x position
    :param y: y position
    :return: None
    """
    global position_x
    global position_y
    position_x = x
    position_y = y


def _set_non_buffered_cursor(x: int, y: int) -> None:
    """
    Set the cursor position in the terminal
    :param x: x position
    :param y: y position
    :return: None
    """
    print("\033[{};{}H".format(y, x), end="")


def draw_line(x: int, y: int, length: int, char: chr) -> None:
    """
    Draw a line
    :param x: x position
    :param y: y position
    :param length: length of the line
    :param char: character to use
    :return: None
    """
    write_at(x, y, char * length)


def draw_column(x: int, y: int, height: int, char: chr) -> None:
    """
    Draw a column
    :param x: x position
    :param y: y position
    :param height: height of the column
    :param char: character to use
    :return: None
    """
    vertical_write_at(x, y, char * height)


def draw_rectangle(x: int, y: int, width: int, height: int, char: chr) -> None:
    """
    Draw a rectangle
    :param x: x position
    :param y: y position
    :param width: width of the rectangle
    :param height: height of the rectangle
    :param char: character to use
    :return: None
    """
    draw_line(x, y, width, char)
    draw_line(x, y + height - 1, width, char)
    draw_column(x, y, height, char)
    draw_column(x + width - 1, y, height, char) #fix the opposite corner of the rectangle


def draw_filled_rectangle(x: int, y: int, width: int, height: int, char: chr) -> None:
    """
    Draw a filled rectangle
    :param x: x position
    :param y: y position
    :param width: width of the rectangle
    :param height: height of the rectangle
    :param char: character to use
    :return: None
    """
    for i in range(height):
        draw_line(x, y + i, width, char)


def compile_buffer() -> None:
    """
    Compile the buffer to a string (optimize the buffer)
    :return: None
    """
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
                buffer[i][j] = buffer[i][j][color_code_lenght+1:]


def _extract_color_from_buffer_cell(x: int, y: int) -> tuple:
    """
    Extract the color data from a buffer cell
    :param x: x position
    :param y: y position
    :return: end index of the color code, color code
    """
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
    return last_color_index,color[:last_color_index + 1]



#
# Key listener
#


pressed_key = []
__should_stop_key_reader_thread__ = False
__should_stop_key_flusher_thread__ = False
config_save = None


def wait_for_key() -> chr:
    """
    Wait for a key to be pressed
    :return: key pressed
    """
    if import_mode == "win":
        return wait_for_key_windows()
    else:
        return wait_for_key_linux()


def wait_for_key_windows():
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
    return key.decode('utf-8')  # convert byte string to string


def wait_for_key_linux():
    key = sys.stdin.read(1)
    if key == "\x1b":
        sys.stdin.read(1) # remove '[' character
        key = sys.stdin.read(1)
        if key == 'A':
            key = 'up'
        elif key == 'B':
            key = 'down'
        elif key == 'C':
            key = 'right'
        elif key == 'D':
            key = 'left'
    return key


def __get_keys_task__() -> None:
    """
    Loop to get the keys
    :return: None
    """
    global pressed_key
    while True:
        key = wait_for_key()
        if key not in pressed_key:
            pressed_key.append(key)
        if __should_stop_key_reader_thread__:
            break


def flush_keys() -> None:
    """
    Flush the pressed keys
    :return: None
    """
    global pressed_key
    pressed_key = []


def __flush_keys_task__(interval: int) -> None:
    """
    Loop to flush the keys
    :param interval: interval between each flush in seconds
    :return: None
    """
    while True:
        flush_keys()
        time.sleep(interval)
        if __should_stop_key_flusher_thread__:
            break


def get_pressed_key() -> list:
    """
    Get the pressed key
    :return: pressed key
    """
    global pressed_key
    return pressed_key


def is_keycode_pressed(key: str) -> bool:
    """
    Check if a key is pressed
    :param key: key to check
    :return: True if the key is pressed, False otherwise
    """
    global pressed_key
    return key in pressed_key


__key_reader_thread__ = threading.Thread(target=__get_keys_task__)
__key_flusher_thread__ = threading.Thread(target=__flush_keys_task__, args=(0.1,))


def start_async_key_listener() -> None:
    """
    Start the async key listener
    :return: None
    """
    if import_mode == "lin":
        global config_save
        config_save = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
    global __key_reader_thread__
    __key_reader_thread__ = threading.Thread(target=__get_keys_task__)
    __key_reader_thread__.start()


def stop_async_key_listener() -> None:
    """
    Stop the async key listener
    :return: None
    """
    if import_mode == "lin":
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, config_save)
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


def set_async_key_listener_interval(interval: int) -> None:
    """
    Set the interval between each key flush
    :param interval: interval in seconds
    :return: None
    """
    global __key_flusher_thread__
    global __should_stop_key_flusher_thread__

    if __key_flusher_thread__.is_alive():
        # Stop the thread
        __should_stop_key_flusher_thread__ = True
        __key_flusher_thread__.join()
        __should_stop_key_flusher_thread__ = False

    __key_flusher_thread__ = threading.Thread(target=__flush_keys_task__, args=(interval,))
    __key_flusher_thread__.start()


def _get_key_code_(key: str) -> chr:
    """
    Get the key code
    :param key: key to get the code
    :return: key code
    """
    if key == "enter":
        return '\r'
    elif key == "esc":
        return '\x1b'
    elif key == "space":
        return ' '
    elif key == "backspace":
        if import_mode == "win":
            return '\x08'
        else:
            return '\x7f'
    elif key == "tab":
        return '\t'
    else:
        return key


def is_key_pressed(key: str) -> bool:
    """
    Check if a key is pressed
    :param key:
    :return:
    """
    global pressed_key
    return is_keycode_pressed(_get_key_code_(key))