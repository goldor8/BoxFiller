import pygame

import grid
from grid import *
from block import rotate_block

title_font = None
large_font = None
screen = None
square_size = 20
empty_square_slot = pygame.transform.scale(pygame.image.load('resources/sprites/square_slot_smooth_down.png'), (square_size, square_size))
filled_square_slot = pygame.transform.scale(pygame.image.load('resources/sprites/square_slot_smooth_up.png'), (square_size, square_size))

background_color = (0, 0, 0)
secondary_color = (255, 0, 0)
text_color = (255, 255, 255)

def is_mouse_on_rect(mouse_pos: pygame.Vector2, rect: pygame.Rect):
    return rect.collidepoint(mouse_pos)

def color_sprite(sprite, color):
    surface = pygame.Surface(sprite.get_size())
    surface.fill(color)
    surface.blit(sprite, (0, 0), special_flags=pygame.BLEND_MULT)
    return surface

def init_display():
    pygame.init()
    global screen
    global title_font
    global large_font
    screen = pygame.display.set_mode((800, 600))
    title_font = pygame.font.Font(None, 80)
    large_font = pygame.font.Font(None, 50)
    pygame.display.set_caption('Game')


def menu():
    init_display()
    global screen
    global large_font
    TitleSurf = title_font.render('Menu', True, text_color)
    TitleRect = TitleSurf.get_rect()
    TitleRect.center = (400, 100)
    PlaySurf = large_font.render('Play', True, text_color)
    PlayRect = PlaySurf.get_rect()
    PlayRect.center = (400, 300)
    RulesSurf = large_font.render('Rules', True, text_color)
    RulesRect = RulesSurf.get_rect()
    RulesRect.center = (400, 400)

    choice = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    choice -= 1
                elif event.key == pygame.K_DOWN:
                    choice += 1
                elif event.key == pygame.K_RETURN:
                    return choice
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return choice
        if choice < 0:
            choice = 1
        elif choice > 1:
            choice = 0

        if is_mouse_on_rect(pygame.mouse.get_pos(), PlayRect):
            choice = 0
        elif is_mouse_on_rect(pygame.mouse.get_pos(), RulesRect):
            choice = 1

        screen.fill(background_color)
        screen.blit(TitleSurf, TitleRect)

        if choice == 0:
            pygame.draw.rect(screen, secondary_color, PlayRect)

        elif choice == 1:
            pygame.draw.rect(screen, secondary_color, RulesRect)

        screen.blit(PlaySurf, PlayRect)
        screen.blit(RulesSurf, RulesRect)

        pygame.display.flip()


def select_grid_type():
    global screen
    global large_font
    TitleSurf = title_font.render('Select Grid Type', True, text_color)
    TitleRect = TitleSurf.get_rect()
    TitleRect.center = (400, 100)
    CircleSurf = large_font.render('Circle', True, text_color)
    CircleRect = CircleSurf.get_rect()
    CircleRect.center = (200, 300)
    TriangleSurf = large_font.render('Triangle', True, text_color)
    TriangleRect = TriangleSurf.get_rect()
    TriangleRect.center = (400, 300)
    LozengeSurf = large_font.render('Lozenge', True, text_color)
    LozengeRect = LozengeSurf.get_rect()
    LozengeRect.center = (600, 300)

    choice = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    choice -= 1
                elif event.key == pygame.K_RIGHT:
                    choice += 1
                elif event.key == pygame.K_RETURN:
                    return choice
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return choice
        if choice < 0:
            choice = 2
        elif choice > 2:
            choice = 0

        if is_mouse_on_rect(pygame.mouse.get_pos(), CircleRect):
            choice = 0
        elif is_mouse_on_rect(pygame.mouse.get_pos(), TriangleRect):
            choice = 1
        elif is_mouse_on_rect(pygame.mouse.get_pos(), LozengeRect):
            choice = 2

        screen.fill(background_color)
        screen.blit(TitleSurf, TitleRect)

        if choice == 0:
            pygame.draw.rect(screen, secondary_color, CircleRect)

        elif choice == 1:
            pygame.draw.rect(screen, secondary_color, TriangleRect)

        elif choice == 2:
            pygame.draw.rect(screen, secondary_color, LozengeRect)

        screen.blit(CircleSurf, CircleRect)
        screen.blit(TriangleSurf, TriangleRect)
        screen.blit(LozengeSurf, LozengeRect)

        pygame.display.flip()


def select_grid_size():
    global screen
    global large_font
    TitleSurf = title_font.render('Select Grid Size', True, text_color)
    TitleRect = TitleSurf.get_rect()
    TitleRect.center = (400, 100)
    SmallSurf = large_font.render('Small', True, text_color)
    SmallRect = SmallSurf.get_rect()
    SmallRect.center = (200, 300)
    MediumSurf = large_font.render('Medium', True, text_color)
    MediumRect = MediumSurf.get_rect()
    MediumRect.center = (400, 300)
    LargeSurf = large_font.render('Large', True, text_color)
    LargeRect = LargeSurf.get_rect()
    LargeRect.center = (600, 300)

    choice = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    choice -= 1
                elif event.key == pygame.K_RIGHT:
                    choice += 1
                elif event.key == pygame.K_RETURN:
                    if choice == 0:
                        return 21
                    elif choice == 1:
                        return 23
                    elif choice == 2:
                        return 25
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if choice == 0:
                        return 21
                    elif choice == 1:
                        return 23
                    elif choice == 2:
                        return 25
        if choice < 0:
            choice = 2
        elif choice > 2:
            choice = 0

        if is_mouse_on_rect(pygame.mouse.get_pos(), SmallRect):
            choice = 0
        elif is_mouse_on_rect(pygame.mouse.get_pos(), MediumRect):
            choice = 1
        elif is_mouse_on_rect(pygame.mouse.get_pos(), LargeRect):
            choice = 2

        screen.fill(background_color)
        screen.blit(TitleSurf, TitleRect)

        if choice == 0:
            pygame.draw.rect(screen, secondary_color, SmallRect)

        elif choice == 1:
            pygame.draw.rect(screen, secondary_color, MediumRect)

        elif choice == 2:
            pygame.draw.rect(screen, secondary_color, LargeRect)

        screen.blit(SmallSurf, SmallRect)
        screen.blit(MediumSurf, MediumRect)
        screen.blit(LargeSurf, LargeRect)

        pygame.display.flip()

def draw_grid(play_grid, offset_x, offset_y):
    for y in range(0, len(play_grid)):
        for x in range(0, len(play_grid[y])):
            if play_grid[y][x] == 1:
                screen.blit(empty_square_slot, (x * 20 + offset_x, y * 20 + offset_y))
            elif play_grid[y][x] == 2:
                screen.blit(color_sprite(filled_square_slot, secondary_color), (x * 20 + offset_x, y * 20 + offset_y))


def draw_available_blocks(available_blocks, offset_x, offset_y, horizontal_space, exclude_index):
    block_per_line = int((horizontal_space / square_size - 2) / len(available_blocks[0]))  # compute the number of block per line
    block_line_index = -1  # init at -1 to increment at the first loop

    for blockIndex in range(0, len(available_blocks)):
        block = available_blocks[blockIndex]

        # limit the number of block per line by adding a new line
        if blockIndex % block_per_line == 0:
            block_line_index += 1

        if blockIndex == exclude_index:
            continue

        # Draw the block
        draw_block(block, offset_x + (blockIndex % block_per_line) * (len(block[0]) + 1) * square_size, offset_y + block_line_index * square_size * (len(block) + 1))

def draw_block(block, offset_x, offset_y):
    for lineIndex in range(0, len(block)):
        line = block[lineIndex]

        # Draw the block line
        for numberIndex in range(0, len(line)):
            number = line[numberIndex]

            if number == 1:
                screen.blit(color_sprite(empty_square_slot, secondary_color), (offset_x + numberIndex * square_size, offset_y + lineIndex * square_size))

selected_block = None
block_position = None
def show_board(play_grid, blocks):
    global screen
    global large_font
    global empty_square_slot

    grid_x_offset = 30
    grid_y_offset = 30

    grab_x_offset = 0
    grab_y_offset = 0

    global selected_block
    selected_block = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    selected_block, grab_x_offset, grab_y_offset = get_block_index_mouse_on(mouse_x, mouse_y, blocks, 60 + len(play_grid[0] * square_size), 30, 400)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if selected_block != -1:
                        mouse_x, mouse_y = event.pos
                        global block_position
                        grid_coord = get_grid_rounded_coord_mouse_on(play_grid, mouse_x - grab_x_offset, mouse_y - grab_y_offset + (len(blocks[selected_block]) - 1) * square_size, grid_x_offset, grid_y_offset)
                        print(grid_coord)
                        if grid.is_in_grid(play_grid, grid_coord[0], grid_coord[1]):
                            block_position = grid_coord
                            return
                        else:
                            selected_block = -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if selected_block != -1:
                        blocks[selected_block] = rotate_block(blocks[selected_block])

        if pygame.mouse.get_pressed(3)[2]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = get_grid_coord_mouse_on(play_grid, mouse_x, mouse_y, grid_x_offset, grid_y_offset)
            if grid.is_in_grid_and_empty(play_grid, grid_x, grid_y):
                play_grid[grid_y][grid_x] = 2

        mouse_x, mouse_y = pygame.mouse.get_pos()

        screen.fill(background_color)

        draw_grid(play_grid, grid_x_offset, grid_y_offset)
        draw_available_blocks(blocks, 60 + len(play_grid[0] * square_size), 30, 400, selected_block)
        if selected_block != -1:
            draw_block(blocks[selected_block], mouse_x - grab_x_offset, mouse_y - grab_y_offset)

        pygame.display.flip()


def get_block_index_mouse_on(mouse_x, mouse_y, blocks, offset_x, offset_y, horizontal_space):
    block_per_line = int((horizontal_space / square_size - 2) / len(blocks[0][0]))  # compute the number of block per line
    block_line_index = -1  # init at -1 to increment at the first loop

    for blockIndex in range(0, len(blocks)):
        block = blocks[blockIndex]

        # limit the number of block per line by adding a new line
        if blockIndex % block_per_line == 0:
            block_line_index += 1

        # verify if the mouse is on the block
        left = offset_x + (blockIndex % block_per_line) * (len(block[0]) + 1) * square_size
        right = left + len(block[0]) * square_size
        top = offset_y + block_line_index * square_size * (len(block) + 1)
        bottom = top + len(block) * square_size
        if mouse_x >= left and mouse_x <= right and mouse_y >= top and mouse_y <= bottom:
            return blockIndex, mouse_x - left, mouse_y - top

    return -1,0,0


def get_grid_rounded_coord_mouse_on(play_grid, mouse_x, mouse_y, offset_x, offset_y):
    x = round((mouse_x - offset_x) / square_size)
    y = round((mouse_y - offset_y) / square_size)
    if x >= 0 and x < len(play_grid[0]) and y >= 0 and y < len(play_grid):
        return x, y
    else:
        return -1, -1


def get_grid_coord_mouse_on(play_grid, mouse_x, mouse_y, offset_x, offset_y):
    x = int((mouse_x - offset_x) / square_size)
    y = int((mouse_y - offset_y) / square_size)
    if x >= 0 and x < len(play_grid[0]) and y >= 0 and y < len(play_grid):
        return x, y
    else:
        return -1, -1


def select_block(round_blocks):
    global selected_block
    return selected_block


def select_block_rotation(selected_block):
    return selected_block


def select_block_position(play_grid, selected_block):
    return block_position


def show_game_over(score):
    global screen
    global large_font

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        screen.fill(background_color)

        text = title_font.render("Game Over", True, text_color)
        screen.blit(text, text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100)))

        text = large_font.render("Score: " + str(score), True, text_color)
        screen.blit(text, text.get_rect(center=(400, 400)))

        pygame.display.flip()