import pygame, random
from pygame.locals import *
from setting.setting import *

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load()

    def load_image(self):
        self.image = pygame.Surface((52, 400)).convert_alpha()
        self.image.fill(transparent)
        y = random.randint(-270, -100)
        self.image.blit(pipe_down, (0, y))
        self.image.blit(pipe_up, (0, y+440))

    def load(self):
        self.load_image()
        self.x = 288
        self.y = 0
        self.rect = Rect(self.x, self.y, 52, 400)
        self.is_last = True
        self.is_score = False

    def update(self):
        self.x -= 1
        self.rect = Rect(self.x, self.y, 52, 400)