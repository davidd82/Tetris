#block.py
import sys, pygame
pygame.init()

class Block:
    def __init__(self, file):
        self.image = pygame.image.load(file)

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


    def draw_block(self, screen):
        self.image = self.aspect_scale(self.image, 700, 700)
        screen.blit(self.image, (321,30))
