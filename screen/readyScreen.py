import pygame
from pygame.locals import *
from setting.setting import *
from sprite.bird import *

class ReadyScreen(object):
    def __init__(self):
        self.load()

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(ready_screen_play_button, (86, 300))
        self.image.blit(ready_screen_title, (55, 100))

    def load(self):
        self.load_image()
        self.bird_groupSingle = pygame.sprite.GroupSingle()
        bird = Bird()
        self.bird_groupSingle.add(bird)
        self.x = 0
        self.y = 0
    
    def update(self, ticks):
        self.load_image()
        self.bird_groupSingle.update(ticks)

    def draw(self, screen):
        self.bird_groupSingle.draw(self.image)
        screen.blit(self.image, (self.x, self.y))