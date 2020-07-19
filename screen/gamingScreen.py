import pygame, math
from pygame.locals import *
from setting.setting import *
from sprite.bird import *
from sprite.pipe import *
from function import *

class GamingScreen(object):
    def __init__(self):
        self.load()

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)

    def load(self):
        self.load_image()
        self.bird_groupSingle = pygame.sprite.GroupSingle()
        bird = Bird()
        bird.is_moving = True
        bird.x = 70
        self.bird_groupSingle.add(bird)
        self.pipe_group = pygame.sprite.Group()
        pipe = Pipe()
        self.pipe_group.add(pipe)
        self.x = 0
        self.y = 0
    
    def update(self, ticks, setting, dead_screen):
        self.load_image()
        self.pipe_manager(setting)
        self.bird_groupSingle.update(ticks)
        self.pipe_group.update()
        self.die(setting, dead_screen)

    def draw(self, screen, setting):
        self.bird_groupSingle.draw(self.image)
        self.pipe_group.draw(self.image)
        if setting.phase == 2:
            self.print_score(setting)
        screen.blit(self.image, (self.x, self.y))

    def pipe_manager(self, setting):
        for pipe in self.pipe_group:
            if pipe.is_last:
                if 288 - pipe.x > 140:
                    pipe.is_last = False
                    new_pipe = Pipe()
                    self.pipe_group.add(new_pipe)
            if pipe.x < -52:
                self.pipe_group.remove(pipe)
            if pipe.x < 144 - 52 and pipe.is_score == False:
                setting.score += 1
                get_point_sound.play()
                pipe.is_score = True

    def die(self, setting, dead_screen):
        if pygame.sprite.spritecollide(self.bird_groupSingle.sprite, self.pipe_group, False, pygame.sprite.collide_mask) or self.bird_groupSingle.sprite.y >= 360:
            if setting.score > setting.best_score:
                setting.best_score = setting.score
            write_txt(setting)
            dead_screen.load()
            collide_sound.play()
            setting.phase = 3

    def print_score(self, setting):
        width = 0
        digital = 0
        if setting.score == 0:
            width = 24
            digital = 1
        else:
            for i in range(0, int(math.log10(setting.score)+1)):
                width += 24
                digital += 1
        score_image = pygame.Surface((width, 44)).convert_alpha()
        score_image.fill(transparent)
        for i in range(0, digital):
            n = int(setting.score%pow(10, i+1)/pow(10, i))
            score_image.blit(gaming_screen_letter[n], (width-i*24-24, 0))
        self.image.blit(score_image, (144-width/2, 70))