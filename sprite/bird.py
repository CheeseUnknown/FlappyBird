import pygame
from pygame.locals import *
from setting.setting import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load()

    def load_image(self):
        self.image = pygame.Surface((48, 48)).convert_alpha()
        self.image.fill(transparent)
        if bird_style == 0:
            if self.image_index == 0:
                self.image.blit(pygame.transform.rotate(bird00, self.angle), (0, 0))
            elif self.image_index == 1:
                self.image.blit(pygame.transform.rotate(bird01, self.angle), (0, 0))
            elif self.image_index == 2:
                self.image.blit(pygame.transform.rotate(bird02, self.angle), (0, 0))
            elif self.image_index == 3:
                self.image.blit(pygame.transform.rotate(bird01, self.angle), (0, 0))
        elif bird_style == 1:
            if self.image_index == 0:
                self.image.blit(pygame.transform.rotate(bird10, self.angle), (0, 0))
            elif self.image_index == 1:
                self.image.blit(pygame.transform.rotate(bird11, self.angle), (0, 0))
            elif self.image_index == 2:
                self.image.blit(pygame.transform.rotate(bird12, self.angle), (0, 0))
            elif self.image_index == 3:
                self.image.blit(pygame.transform.rotate(bird11, self.angle), (0, 0))
        elif bird_style == 2:
            if self.image_index == 0:
                self.image.blit(pygame.transform.rotate(bird20, self.angle), (0, 0))
            elif self.image_index == 1:
                self.image.blit(pygame.transform.rotate(bird21, self.angle), (0, 0))
            elif self.image_index == 2:
                self.image.blit(pygame.transform.rotate(bird22, self.angle), (0, 0))
            elif self.image_index == 3:
                self.image.blit(pygame.transform.rotate(bird21, self.angle), (0, 0))

    def load(self):
        self.image_index = 0
        self.last_tick = 0
        self.x = 120
        self.y = 232
        self.rect = Rect(self.x, self.y, 48, 48)
        self.velocity = 0
        self.is_moving = False
        self.angle = 0
        self.load_image()

    def update(self, ticks):
        self.load_image()
        self.circulate_image(ticks)
        self.load_action()
        self.rect = Rect(self.x, self.y, 48, 48)

    def circulate_image(self, ticks):
        if ticks > self.last_tick + 350:
            self.image_index += 1
            if self.image_index == 4:
                self.image_index = 0
            self.last_tick = ticks

    def load_action(self):
        if self.is_moving:
            self.velocity += 0.08
            self.y += self.velocity
            self.angle = -60 * (self.velocity/5) + 50
            if self.angle > 30:
                self.angle = 30
            elif self.angle < -60:
                self.angle = -60
            self.x = 70 + 24 - self.image.get_width()/2
            self.y = self.y + 24 - self.image.get_height()/2