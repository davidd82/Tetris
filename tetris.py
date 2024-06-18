import sys, pygame
import block
pygame.init()

# Set screen size of the window for the tetris game
screen = pygame.display.set_mode((1024, 768))

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

# Rescales the board sprite without making it looked smooshed or stretched
board = aspect_scale(board, 700, 700)

# Create instance of board display
block1 = pygame.image.load(NUM_2_BLOCK[1])

# Board is (381 W X 700 H) after scaling
# Board is (20 H X 10 W)

# Main game loop
while True:

    # QUIT the game if the X in the window is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Fill the screen with black
    screen.fill(black)

    # Map the pixels of the board sprite onto the screen
    # Map towards the center of the screen
    screen.blit(board, (321,30))

    block1 = aspect_scale(block1, 120, 120)
    screen.blit(block1, (321,30))

    # Actually display the entire screen once all the pixels have been mapped
    pygame.display.flip()

