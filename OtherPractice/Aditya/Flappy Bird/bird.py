import pygame as p
from pygame.sprite import _Group
p.init()

# sprite class is a special moving class provided by pygame
#we inherit sprite class
class bird(p.sprite.Sprite):
    def __init__(self):
        super(self,bird).__init__()
        self.img_list = [p.image.load("birdup.png").convert_alpha(),p.image.load("birdown.png").convert_alpha()]
        # a list to store the images
        # convert_alpha to make image in transperancy mode
        self.image_index = 0
        # because initially image will be birdup
        self.image = self.img_list[self.image_index]

        # create a box around bird like we did for backgrounds
        self.rect = self.image.get_rect(center=(100, 100))




