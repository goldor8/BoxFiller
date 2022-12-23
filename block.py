"""
Project : BoxFiller
Description : This module is used to load and manipulate blocks
Author : Brisset Dimitri, Occhiminuti Marius
"""

def load_block(path):  # returns a block from a file
    block = []
    with open(path, "r") as block_1:
        lines = block_1.readlines()
        for i in range(len(lines)):
            block.append([])
            line_numbers = lines[i].split(" ")
            for number in line_numbers:
                block[i].append(int(number))
    return block


def rotate_block(block):  # rotate block by 90°
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


def normalize_block_list(block_list):  # put all block at the same size
    max_side = 0
    for block in block_list:
        if len(block) > max_side:
            max_side = len(block)
        if len(block[0]) > max_side:
            max_side = len(block[0])
    for i in range(len(block_list)):
        normalize_block(block_list[i], max_side, max_side)


def normalize_block(block, height, width):  # set a block to a given size filling with 0
    initial_height = len(block)
    initial_width = len(block[0])
    for i in range(height - initial_height):
        block.insert(0, [0] * initial_width)
    for i in range(len(block)):
        for j in range(width - initial_width):
            block[i].append(0)


def wrap_block(block):  # wrap a block in a list (remove entirely empty lines and columns)
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
            for j in range(len(block) - 1, -1, -1):  # reverse loop to avoid index error because of pop
                block[j].pop(i)
        else:
            break
