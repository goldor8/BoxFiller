def load_block(path):
    M = []
    with open(path, "r") as block_1 :
        lignes =  block_1.readlines()
        for i in range (len(lignes)) :
            M.append([])
            line_numbers = lignes[i].split(" ")
            for number in line_numbers :
                M[i].append(int(number))
    return M


# rotate block by 90°
def rotate_block(M):
    M_rotated = []
    for i in range(len(M[0])):
        M_rotated.append([])
        for j in range(len(M)):
            M_rotated[i].append(M[len(M) - j - 1][i])
    return M_rotated