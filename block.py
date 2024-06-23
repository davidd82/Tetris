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
        self.mini_coord1 = [(4,0),(4,1),(4,2),(4,3)] # BLUE I

        # Update the state of the board using mini_coord
        self.state = state
        for i in range (4):
            self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1
        
        # Checks if the block can no longer go left, right, down, or rotate
        self.out_of_bounds_down = False
        self.out_of_bounds_left = False
        self.out_of_bounds_right = False
        self.out_of_bounds_rotate = False

        # Different rotate coordinate update depending on initial position
        self.rotate_state = 0

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
        if (self.out_of_bounds_down == False):
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
                    self.out_of_bounds_down = True
            
            # Update the state of the board using mini_coord
            # Place that block is arriving will become occupied
            if (self.out_of_bounds_down == False):
                for i in range (4):
                    self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

                self.rect = self.rect.move(0, 34)
                screen.blit(self.image,self.rect)
        
    # Move the rect box of the block 34 pixels to the left
    def block_left(self,screen):
        # Checks if the block is out of bounds
        self.out_of_bounds_right = False
        if (self.out_of_bounds_left == False):
        # Update the state of the board using mini_coord
            # Place that block is leaving will become unoccupied
            for i in range (4):
                self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 0

            # Check which block is being moved
            if (self.block_num == 1):
                # Update the coordinate of the mini blocks to go one col left
                for i in range (4):
                    # Workaround to update a tuple by converting it to list
                    self.temp = list(self.mini_coord1[i])
                    self.temp[0] -= 1
                    self.mini_coord1[i] = tuple(self.temp)

                    # Check if the shape went out of bounds
                    if (self.mini_coord1[i][0] == 0):
                        self.out_of_bounds_left = True
            elif (self.block_num == 7):
                # Update the coordinate of the mini blocks to go one col left
                for i in range (4):
                    # Workaround to update a tuple by converting it to list
                    self.temp = list(self.mini_coord[i])
                    self.temp[0] -= 1
                    self.mini_coord[i] = tuple(self.temp)

                    # Check if the shape went out of bounds
                    if (self.mini_coord[i][0] == 0):
                        self.out_of_bounds_left = True
            
            # Update the state of the board using mini_coord
            # Place that block is arriving will become occupied
            if (self.out_of_bounds_left == False):
                for i in range (4):
                    self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

            self.rect = self.rect.move(-34,0)
            screen.blit(self.image,self.rect)

    # Move the rect box of the block 34 pixels to the right
    def block_right(self,screen):
        # Checks if the block is out of bounds
        self.out_of_bounds_left = False
        if (self.out_of_bounds_right == False):
        # Update the state of the board using mini_coord
            # Place that block is leaving will become unoccupied
            for i in range (4):
                self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 0

            # Check which block is being moved
            if (self.block_num == 1):
                # Update the coordinate of the mini blocks to go one col left
                for i in range (4):
                    # Workaround to update a tuple by converting it to list
                    self.temp = list(self.mini_coord1[i])
                    self.temp[0] += 1
                    self.mini_coord1[i] = tuple(self.temp)

                    # Check if the shape went out of bounds
                    if (self.mini_coord1[i][0] == 9):
                        self.out_of_bounds_right = True
            elif (self.block_num == 7):
                # Update the coordinate of the mini blocks to go one col right
                for i in range (4):
                    # Workaround to update a tuple by converting it to list
                    self.temp = list(self.mini_coord[i])
                    self.temp[0] += 1
                    self.mini_coord[i] = tuple(self.temp)

                    # Check if the shape went out of bounds
                    if (self.mini_coord[i][0] == 9):
                        self.out_of_bounds_right = True
                
            # Update the state of the board using mini_coord
            # Place that block is arriving will become occupied
            if (self.out_of_bounds_right == False):
                for i in range (4):
                    self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

            self.rect = self.rect.move(34,0)
            screen.blit(self.image,self.rect)

    # Rotates the block 90 degrees
    def block_rotate(self,screen):
        # Update the state of the board using mini_coord
        # Place that block is leaving will become unoccupied
        if (self.out_of_bounds_rotate == False):
            for i in range (4):
                self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 0

            # Update each mini block's coordinate for rotate
            if (self.rotate_state == 0):
                # Workaround to update a tuple by converting it to list
                self.temp = list(self.mini_coord[0])
                self.temp[0] += 1
                self.mini_coord[0] = tuple(self.temp)

                self.temp = list(self.mini_coord[1])
                self.temp[1] += 1
                self.mini_coord[1] = tuple(self.temp)

                self.temp = list(self.mini_coord[3])
                self.temp[1] += 1
                self.temp[0] -= 2
                self.mini_coord[3] = tuple(self.temp)

                self.rotate_state = 1
            elif (self.rotate_state == 1): # Different rotate depending on position
                # Workaround to update a tuple by converting it to list
                self.temp = list(self.mini_coord[0])
                self.temp[0] -= 1
                self.mini_coord[0] = tuple(self.temp)

                self.temp = list(self.mini_coord[1])
                self.temp[1] -= 1
                self.mini_coord[1] = tuple(self.temp)

                self.temp = list(self.mini_coord[3])
                self.temp[1] -= 1
                self.temp[0] += 2
                self.mini_coord[3] = tuple(self.temp)

                self.rotate_state = 0


            for i in range (4):
                # Check if the shape went out of bounds
                if (self.mini_coord[i][0] == 10):
                    self.out_of_bounds_rotate = True

                # Check if the shape went out of bounds
                if (self.mini_coord[i][0] == -1):
                    self.out_of_bounds_rotate = True
                    
                # Check if the shape went out of bounds
                if (self.mini_coord[i][1] == 21):
                    self.out_of_bounds_rotate = True
                    
            # Update the state of the board using mini_coord
            # Place that block is arriving will become occupied
            if (self.out_of_bounds_rotate == False):
                for i in range (4):
                    self.state[self.mini_coord[i][0]][self.mini_coord[i][1]] = 1

                # A rotate will allow one more movement to the right
                self.out_of_bounds_right = False

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
            elif (self.out_of_bounds_right == True): # Possible that a rotate is not possible if state is 1
                # Workaround to update a tuple by converting it to list
                # Reset the position of each mini_coord and DONT rotate image
                self.temp = list(self.mini_coord[0])
                self.temp[0] += 1
                self.mini_coord[0] = tuple(self.temp)

                self.temp = list(self.mini_coord[1])
                self.temp[1] += 1
                self.mini_coord[1] = tuple(self.temp)

                self.temp = list(self.mini_coord[3])
                self.temp[1] += 1
                self.temp[0] -= 2
                self.mini_coord[3] = tuple(self.temp)

                # Rotate is no longer out of bounds
                self.out_of_bounds_rotate = False

                # The state is still 1
                self.rotate_state = 1


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



    
