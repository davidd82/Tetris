#block.py
import pygame
pygame.init()

class Block:
    def __init__(self, file, block_num):
        # Load the image from the given file
        self.image = pygame.image.load(file)

        # Store block num
        self.block_num = block_num

        # Scale the block depending on which block it is
        if (self.block_num == 1):
            height = 135
            width  = 135
        elif (self.block_num == 2):
            height = 102
            width = 102
        elif (self.block_num == 3):
            height = 102
            width = 102
        elif (self.block_num == 4):
            height = 67
            width = 67
        elif (self.block_num == 5):
            height = 102
            width = 102
        elif (self.block_num == 6):
            height = 100
            width = 100
        elif (self.block_num == 7):
            height = 102
            width = 102

        # Resize the image while keeping aspect ratio
        self.image = self.aspect_scale(self.image, width, height)

        # Get rect of the resized image
        self.rect = self.image.get_rect()

        # Place the block at top and center of board
        # Different coordinate depending on the type of block
        if (self.block_num == 1):
            self.rect.y = 11
            self.rect.x = 492
        elif (self.block_num == 2):
            self.rect.y = 11
            self.rect.x = 492
        elif (self.block_num == 3):
            self.rect.y = 11
            self.rect.x = 492
        elif (self.block_num == 4):
            self.rect.y = 11
            self.rect.x = 492
        elif (self.block_num == 5):
            self.rect.y = 11
            self.rect.x = 492
        elif (self.block_num == 6):
            self.rect.y = 12
            self.rect.x = 493
        elif (self.block_num == 7):
            self.rect.y = 11
            self.rect.x = 492

    # Handles drawing the block onto the screen
    def draw_block(self, screen):
        self.rect = self.block_fall()
        screen.blit(self.image, self.rect)

    # Move the rect box of the block 34 pixels down
    def block_fall(self):
        return self.rect.move(0, 34)

    # Scales the passed image to the pixel size while maintaining the aspect ratio
    def aspect_scale(self,img, bx, by):
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



    
