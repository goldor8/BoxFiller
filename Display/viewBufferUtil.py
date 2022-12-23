"""
Project : BoxFiller
Description : Utility module for display using a view buffer (list of string)
Author : Brisset Dimitri
"""

viewLine = 0


def set_line_view(line: int) -> None:
    """
    Set the line where the next add_to_view will be added
    :param line: the line to set
    :return: None
    """
    global viewLine
    viewLine = line


def increment_view_line() -> None:
    """
    Increment the line where the next add_to_view will be added
    :return: None
    """
    global viewLine
    viewLine += 1


def add_to_view(text: str, view: list) -> None:
    """
    Add a test to the view
    :param text: the text to add
    :param view: the view to add the text to
    :return: None
    """
    if viewLine >= len(view):
        for i in range(len(view), viewLine + 1):
            view.append("")
    view[viewLine] = view[viewLine] + text


def add_line_to_view(line: str, view: list) -> None:
    """
    Add a line to the view
    :param line: the line to add
    :param view: the view to add the line to
    :return:
    """
    global viewLine
    view.append(line)
    viewLine += 1


def show_view(view: list) -> None:
    """
    Display the view to the console
    :param view: the view to display
    :return: None
    """
    for line in view:
        print(line)


def clear_view(view: list) -> None:
    """
    Clear the view
    :param view: the view to clear
    :return: None
    """
    view.clear()
