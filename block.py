"""
Project : BoxFiller
Description : This module is used to load and manipulate blocks
Author : Brisset Dimitri, Occhiminuti Marius
"""
import os


def load_block(path: str) -> list:
    """
    Load a block from a file
    :param path: path to the file
    :return: the block contained in the file
    """
    with open("Level/Blocks/" + path, 'r') as f:
        block = []
        for line in f:
            block.append([int(x) for x in line.split(" ")])
        return block


def rotate_block(block: list) -> list:
    """
    Rotate a block by 90° 
    :param block: the block to rotate
    :return: the rotated block
    """

    # the block is wrapped when rotated to let the block in the bottom left corner
    initial_size = len(block)
    wrapped_block = block.copy()
    wrap_block(wrapped_block)
    wrapped_width = len(wrapped_block[0])
    wrapped_height = len(wrapped_block)

    rotated_block = []
    for i in range(wrapped_width):
        rotated_block.append([])
        for j in range(wrapped_height):
            rotated_block[i].append(wrapped_block[wrapped_height - 1 - j][i])
    normalize_block(rotated_block, initial_size, initial_size)
    return rotated_block


def normalize_block_list(block_list: list) -> None:
    """
    Normalize a list of blocks to the same size
    :param block_list: the list of blocks to normalize
    :return: list is modified by reference
    """
    max_side = 0
    for block in block_list:
        if len(block) > max_side:
            max_side = len(block)
        if len(block[0]) > max_side:
            max_side = len(block[0])
    for i in range(len(block_list)):
        normalize_block(block_list[i], max_side, max_side)


def normalize_block(block: list, height: int, width: int) -> None:
    """
    Normalize a block to a given size (add empty lines and columns)
    :param block: block to normalize
    :param height: height of the normalized block
    :param width: width of the normalized block
    :return: the block is modified by reference
    """
    initial_height = len(block)
    initial_width = len(block[0])
    for i in range(height - initial_height):
        block.insert(0, [0] * initial_width)
    for i in range(len(block)):
        for j in range(width - initial_width):
            block[i].append(0)


def wrap_block(block: list) -> None:
    """
    Wrap a block in a list (remove entirely empty lines and columns)
    :param block: the block to wrap
    :return: the block is modified by reference
    """
    # remove empty lines
    i = 0
    while i < len(block):
        if sum(block[i]) == 0:
            block.pop(i)
            i -= 1
        else:
            break
        i += 1

    # remove empty columns
    width = len(block[0])
    for i in range(width-1, -1, -1):  # reverse loop because we remove only last empty columns elements
        if sum([block[j][i] for j in range(len(block))]) == 0:
            for j in range(len(block)):  # reverse loop to avoid index error because of pop
                block[j].pop(i)
        else:
            break


def get_block_paths_for_board_choice(choice: int) -> list:
    """
    Get the paths of blocks corresponding to the choice of board
    :param choice: the choice of board (0 = circle, 1 = triangle, 2 = lozenge)
    :return: the paths of blocks corresponding to the choice of board
    """
    grid_blocks = ["common/" + i for i in os.listdir("Level/Blocks/common")]
    if choice == 0:
        grid_blocks += ["circle/" + i for i in os.listdir("Level/Blocks/circle")]
    elif choice == 1:
        grid_blocks += ["triangle/" + i for i in os.listdir("Level/Blocks/triangle")]
    elif choice == 2:
        grid_blocks += ["lozenge/" + i for i in os.listdir("Level/Blocks/lozenge")]
    return grid_blocks


def get_blocks_from_files(blocks_path: list) -> list:
    """
    Get the blocks from a list of paths
    :param blocks_path: paths of files containing blocks
    :return: the blocks contained in the files
    """
    block_list = []
    for block_path in blocks_path:
        block_list.append(load_block(block_path))
    return block_list
