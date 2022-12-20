def load_block(path):
    block = []
    with open(path, "r") as block_1 :
        lines =  block_1.readlines()
        for i in range (len(lines)) :
            block.append([])
            line_numbers = lines[i].split(" ")
            for number in line_numbers :
                block[i].append(int(number))
    return block


# rotate block by 90°
def rotate_block(M):
    M_rotated = []
    for i in range(len(M[0])):
        M_rotated.append([])
        for j in range(len(M)):
            M_rotated[i].append(M[len(M) - j - 1][i])
    return M_rotated