import sys, pygame
import block
import random
pygame.init()

# Set screen size of the window for the tetris game
screen = pygame.display.set_mode((1024, 768))

# Get clock of the game
clock = pygame.time.Clock()

# black color code
black = 0, 0, 0

# Array of file locations for block sprites 
NUM_2_BLOCK = {
    1 : "./sprites/Shape Blocks/I.png",
    2 : "./sprites/Shape Blocks/J.png",
    3 : "./sprites/Shape Blocks/L.png",
    4 : "./sprites/Shape Blocks/O.png",
    5 : "./sprites/Shape Blocks/S.png",
    6 : "./sprites/Shape Blocks/T.png",
    7 : "./sprites/Shape Blocks/Z.png",
}

# Loads the tetris board sprite and stores is as "board"
board = pygame.image.load("./sprites/Board/Board.png")

# Scales the passed image to the pixel size while maintaining the aspect ratio
def aspect_scale(img, bx, by):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (sx,sy))

# Rescales the board sprite without making it look smooshed or stretched
board = aspect_scale(board, 750, 750)

# Create instance of block
block_num = 3
block1 = block.Block(NUM_2_BLOCK[block_num], block_num)

# Board is (381 W X 700 H) after scaling
# Board is (20 H X 10 W)

# Main game loop
while True:

    # QUIT the game if the X in the window is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Get a random number to choose next block
    ran = random.randrange(1, 7)

    # Fill the screen with black
    screen.fill(black)

    # Map the pixels of the board sprite onto the screen
    # Map towards the center of the screen
    screen.blit(board, (321,10))

    # Draw the current block
    block1.draw_block(screen)

    # Actually display the entire screen once all the pixels have been mapped
    pygame.display.flip()

    clock.tick(1)

