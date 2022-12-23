"""
Project : BoxFiller
Description : Utility module for display using a view buffer (list of string)
Author : Brisset Dimitri
"""

viewLine = 0


def set_line_view(line):
    global viewLine
    viewLine = line


def increment_view_line():
    global viewLine
    viewLine += 1


def add_to_view(value, view):
    if viewLine >= len(view):
        for i in range(len(view), viewLine + 1):
            view.append("")
    view[viewLine] = view[viewLine] + value


def add_line_to_view(line, view):
    global viewLine
    view.append(line)
    viewLine += 1


def show_view(view):
    for line in view:
        print(line)


def clear_view(view):
    view.clear()
