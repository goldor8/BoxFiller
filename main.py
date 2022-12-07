import grid
import termilib

use_termilib = False
grid = []
gridView = []
blockView = []


def main():
    print("Welcome to BoxFiller !")
    ##menu()
    board = grid.create_circle_grid(21)
    grid.fill_all_grid(board)
    show_grid(board)
    grid.check_for_full_row_or_column(board)
    show_grid(board)
    input("Press any key to continue")


def init_game():
    gridType = select_grid_type()
    gridSize = select_grid_size()

    global grid
    if gridType == "1":
        grid = grid.create_circle_grid(gridSize)
    elif gridType == "2":
        grid = grid.create_triangle_grid(gridSize)
    elif gridType == "3":
        gird = grid.create_lozenge_grid(gridSize)


def show_board(grid):
    return


def playLoop():
    show_board(grid)


    playLoop()


def compute_score(bloc_casse):
    score = bloc_casse ** 2
    return score

#
# Interface proxy
#


def show_grid(grid):
    if use_termilib:
        show_grid_termilib(grid)
    else:
        show_grid_basic(grid)


def select_grid_type():
    if use_termilib:
        return select_grid_type_termilib()
    else:
        return select_grid_type_basic()


def select_grid_size():
    if use_termilib:
        return select_grid_size_termilib()
    else:
        return select_grid_size_basic()


def menu():
    if use_termilib:
        menu_termilib()
    else:
        menu_basic()


def show_rules() :
    if use_termilib:
        show_rules_termilib()
    else:
        show_rules_basic()


#
# Basic Terminal Interface
#

viewLine = 0

def set_line_view(line):
    global viewLine
    viewLine = line

def increment_view_line():
    global viewLine
    viewLine += 1

def add_to_view(value, view):
    if (viewLine >= len(view)):
        for i in range(len(view), viewLine):
            gridView.append([])
    view[viewLine] = view[viewLine] + value

def add_line_to_view(line, view):
    view.append(line)
    viewLine += 1


def show_view(view):
    for line in view:
        print(line)

def clear_view(view):
    view.clear()


def show_grid_basic(grid):
    set_line_view(0)
    print("    ", end="")
    add_to_view("    ", gridView)
    for i in range(len(grid[0])):
        print(chr(65 + i), end="  ")
        add_to_view(chr(65 + i) + "  ", gridView)
    print()
    increment_view_line()
    print("  ╔", end="")
    add_to_view("  ╔", gridView)
    for i in range(len(grid[0])):
        print("═══", end="")
        add_to_view("═══", gridView)
    print("╗", end="")
    add_to_view("╗", gridView)
    print()
    increment_view_line()
    for y in range (len(grid)):
        print(chr(97 + y), "║", end="")
        add_to_view(chr(97 + y) + "║", gridView)
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                print(".  ", end="")
                add_to_view(".  ", gridView)
            elif grid[y][x] == 2:
                print("■  ", end="")
                add_to_view("■  ", gridView)
            elif grid[y][x] == 0:
                print("   ", end="")
                add_to_view("   ", gridView)
        print("║")
        add_to_view("║", gridView)
        increment_view_line()
    print("  ╚" , end="")
    add_to_view("  ╚", gridView)
    for  i in range (len(grid[0])):
        print("═══", end="")
        add_to_view("═══", gridView)
    print("╝")
    add_to_view("╝", gridView)
    increment_view_line()
    print("view mode")
    show_view(gridView)


def select_grid_type_basic():
    print("Select grid type :")
    print("1. Circle")
    print("2. Triangle")
    print("3. Lozenge")

    gridType = input("Enter your choice : ")
    while gridType not in ["1", "2", "3"]:
        print("Invalid choice !")
        gridType = input("Enter your choice : ")

    return gridType


def select_grid_size_basic():
    print("Select grid odd size between 21 and 43 : ")
    gridSize = int(input("Enter your choice : "))
    while gridSize not in range(21, 44) or gridSize % 2 == 0:
        print("Invalid choice !")
        gridSize = int(input("Enter your choice : "))

    return gridSize


def menu_basic():
    print("Select what you want to do")
    print("1. Play")
    print("2. Show rules")

    choice = int(input("Enter your choice : "))
    while choice != 1 and choice != 2:
        choice = int(input("Invalid choice ! Enter your choice : "))
    if choice == 1:
        init_game()
    elif choice == 2:
        show_rules()


def show_rules_basic() :
    print("règles")
    input("Press any key to continue")
    menu()

#
# Custom Termilib Interface
#


def show_grid_termilib(grid):
    termilib.set_background_color(termilib.colors["blue"])
    termilib.draw_rectangle(5, 2, len(grid[0])+2, len(grid)+2, " ")
    termilib.set_background_color(termilib.colors["black"])
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            termilib.set_cursor_position(x+6, y+3)
            if grid[y][x] == 1:
                termilib.write("-")
            elif grid[y][x] == 2:
                termilib.write("#")
    return


def select_grid_type_termilib():
    #todo
    return


def select_grid_size_termilib():
    #todo
    return


def menu_termilib():
    #todo
    return


def show_rules_termilib() :
    #todo
    return



if __name__ == "__main__":
    main()