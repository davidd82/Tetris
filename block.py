#block.py
import pygame
pygame.init()

class Block:
    def __init__(self, file, block_num, state):
        # Load the image from the given file
        self.image = pygame.image.load(file)

        # Store block num
        self.block_num = block_num

        # Stores the coordinates of the mini blocks
        self.mini_coord = [(4,0), (5,0), (5,1), (6,1)] # RED Z

        # Update the state of the board using mini_coord
        self.state = state
        for i in range (4):
            self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

        self.out_of_bounds = False

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
            self.rect.y = 45
            self.rect.x = 492
        elif (self.block_num == 2):
            self.rect.y = 45
            self.rect.x = 492
        elif (self.block_num == 3):
            self.rect.y = 45
            self.rect.x = 492
        elif (self.block_num == 4):
            self.rect.y = 45
            self.rect.x = 492
        elif (self.block_num == 5):
            self.rect.y = 45
            self.rect.x = 492
        elif (self.block_num == 6):
            self.rect.y = 46
            self.rect.x = 493
        elif (self.block_num == 7):
            self.rect.y = 45
            self.rect.x = 492

    # Handles drawing the block onto the screen
    def draw_block(self, screen):
        screen.blit(self.image, self.rect)

    # Move the rect box of the block 34 pixels down
    def block_fall(self,screen):
        # Checks if the block is out of bounds
        if (self.out_of_bounds == False):
            # Update the state of the board using mini_coord
            # Place that block is leaving will become unoccupied
            for i in range (4):
                self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 0

            # Update the coordinate of the mini blocks to go one row down
            for i in range (4):
                # Workaround to update a tuple by converting it to list
                self.temp = list(self.mini_coord[i])
                self.temp[1] += 1
                self.mini_coord[i] = tuple(self.temp)

                # Check if the shape went out of bounds
                if (self.mini_coord[i][1] == 20):
                    self.out_of_bounds = True
            
            # Update the state of the board using mini_coord
            # Place that block is arriving will become occupied
            if (self.out_of_bounds == False):
                for i in range (4):
                    self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

                self.rect = self.rect.move(0, 34)
                screen.blit(self.image,self.rect)
        
    # Move the rect box of the block 34 pixels to the left
    def block_left(self,screen):
        self.rect = self.rect.move(-34,0)
        screen.blit(self.image,self.rect)

    # Move the rect box of the block 34 pixels to the right
    def block_right(self,screen):
        self.rect = self.rect.move(34,0)
        screen.blit(self.image,self.rect)

    # Rotates the block 90 degrees
    def block_rotate(self,screen):
        # Store the current position of rect
        y = self.rect.y
        x = self.rect.x

        # Rotate the image and update
        self.image = pygame.transform.rotate(self.image, 90)

        # Get the rect of updated/rotated image
        self.rect = self.image.get_rect()

        # Set the position of this new rect to the position of the old rect
        self.rect.y = y
        self.rect.x = x

        # Map the pixels
        screen.blit(self.image,self.rect)

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



    
