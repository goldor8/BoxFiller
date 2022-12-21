# block management module

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
    rotated_block = []
    for i in range(len(block)):
        rotated_block.append([])
        for j in range(len(block[i])):
            rotated_block[i].append(block[len(block) - 1 - j][i])
    return rotated_block
