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
print(load_block())
