import os

position_x = 0
position_y = 0
size_x = 0
size_y = 0
fg_color = "\033[38;5;255m"
bg_color = "\033[48;5;0m"

buffer = []
colors = {"black": 0, "blue": 21, "green": 40, "cyan": 44, "red": 160, "purple": 127, "yellow": 226, "white": 250, "gray": 244, "lightblue": 33, "lightgreen": 82, "lightcyan": 45, "lightred": 192, "lightpurple": 128, "lightyellow": 227, "brightwhite": 255}


def set_terminal_size(cols, rows):
    global buffer
    for i in range(rows):
        buffer.append(["{}{} ".format(fg_color, bg_color)] * (cols))
    os.system('mode con: cols={} lines={}'.format(cols, rows))
    global size_x
    global size_y
    size_y = rows
    size_x = cols


def get_terminal_size():
    return size_x, size_y


def move_cursor_at(x,y):
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
    print(fg_color+bg_color, end="")


def render():
    global buffer
    set_cursor_position(0, 0)
    lines = []
    for i in range(len(buffer)):
        lines.append("".join(buffer[i]))
    print("\n".join(lines), end="")


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
    draw_column(x + width - 1, y, height, char) #fix the opposite corner of the rectangle


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
                buffer[i][j] = buffer[i][j][color_code_lenght+1:]


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
    return last_color_index,color[:last_color_index + 1]