import sys, pygame
import block
import random
import numpy as np 

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

# Sets size of 2D array
state = np.zeros((10,20))

# Rescales the board sprite without making it look smooshed or stretched
board = aspect_scale(board, 750, 750)

# Create instance of block
block_num = 7
block1 = block.Block(NUM_2_BLOCK[block_num], block_num, state)

# Board is (381 W X 700 H) after scaling
# Board is (20 H X 10 W)

# count is used to control speed of fall
# Allows for higher fps for checking user input
count = 0

# Controls movement speed of block from user input (not too fast and not too slow)
move_ticker = 0



# Main game loop
while True:

    # QUIT the game if the X in the window is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # Checks if a button has been pressed
    keys=pygame.key.get_pressed()
    # Move block DOWN and RIGHT and ROTATE
    if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and keys[pygame.K_z]: 
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_fall(screen)
            block1.block_right(screen)
            block1.block_rotate(screen)
    # Move block DOWN and LEFT and ROTATE
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and keys[pygame.K_z]:
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_fall(screen)
            block1.block_left(screen)
            block1.block_rotate(screen)
    # Move block DOWN and RIGHT
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]: 
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_fall(screen)
            block1.block_right(screen)
    # Move block DOWN and LEFT
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_fall(screen)
            block1.block_left(screen)
    # Move block DOWN and ROTATE
    elif keys[pygame.K_DOWN] and keys[pygame.K_z]:
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_fall(screen)
            block1.block_rotate(screen)
    # Move block RIGHT and ROTATE
    elif keys[pygame.K_RIGHT] and keys[pygame.K_z]: 
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_right(screen)
            block1.block_rotate(screen)
    # Move block LEFT and ROTATE
    elif keys[pygame.K_LEFT] and keys[pygame.K_z]: 
        if move_ticker <= 0:   
            move_ticker = 5
            block1.block_left(screen)
            block1.block_rotate(screen)
    # Move block LEFT
    elif keys[pygame.K_LEFT]:
        if move_ticker <= 0:
            move_ticker = 15
            block1.block_left(screen)
    # Move block RIGHT
    elif keys[pygame.K_RIGHT]: 
        if move_ticker <= 0:   
            move_ticker = 15
            block1.block_right(screen)
    # Move block DOWN
    elif keys[pygame.K_DOWN]: 
        if move_ticker <= 0:   
            move_ticker = 3
            block1.block_fall(screen)
    # ROTATE block
    elif keys[pygame.K_z]: 
        if move_ticker <= 0:   
            move_ticker = 10
            block1.block_rotate(screen)

    # Get a random number to choose next block
    ran = random.randrange(1, 7)

    # Fill the screen with black
    screen.fill(black)

    # Map the pixels of the board sprite onto the screen
    # Map towards the center of the screen
    screen.blit(board, (321,10))

    # Draw the current block
    block1.draw_block(screen)

    # Drop the block at given speed
    if(count >= 60):
        block1.block_fall(screen)
        count = 0

    # Update the time until next user input is allowed
    if move_ticker > 0:
        move_ticker -= 1

    # Update the time until next block drop
    count += 1

    # Actually display the entire screen once all the pixels have been mapped
    pygame.display.flip()

    # Game runs at 60 fps
    clock.tick(60) #200

