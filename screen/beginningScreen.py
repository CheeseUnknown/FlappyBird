import pygame
from pygame.locals import *
from setting.setting import *
from sprite.bird import *

class BeginningScreen(object):
    def __init__(self):
        self.load()

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(beginning_screen_tutorial, (87, 280))
        self.image.blit(beginning_screen_ready, (46, 100))

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