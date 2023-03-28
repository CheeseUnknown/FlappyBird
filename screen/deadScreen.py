import pygame, math
from pygame.locals import *
from setting.setting import *

class DeadScreen(object):
    def __init__(self):
        self.load()

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(dead_screen_game_over, (45, 96))

    def load(self):
        self.load_image()
        self.x = 0
        self.y = 0
        self.score_board_y = 0
        self.medal_image = pygame.Surface((44, 44)).convert_alpha()
        self.medal_image.fill(transparent)
        self.alpha = 0

    def update(self):
        self.load_image()

    def draw(self, screen, setting):
        self.score_board_appear(setting)
        self.restart_button_appear()
        screen.blit(self.image, (self.x, self.y))

    def score_board_appear(self, setting):
        if self.score_board_y < 193:
            self.score_board_y += 2.5
        self.image.blit(dead_screen_score_board, (25, self.score_board_y))
        if self.score_board_y >= 193:
            #medal
            self.medal_image.set_alpha(self.alpha)
            if setting.score < 10:
                self.medal_image.blit(dead_screen_bronze_medal, (0, 0))
            elif setting.score < 20:
                self.medal_image.blit(dead_screen_silver_medal, (0, 0))
            else:
                self.medal_image.blit(dead_screen_gold_medal, (0, 0))
            if self.alpha < 255:
                self.alpha += 3
            self.image.blit(self.medal_image, (57, 240))
            #score
            self.print_score(setting)
            self.print_best_score(setting)

    def print_score(self, setting):
        width = 0
        digital = 0
        if setting.score == 0:
            width = 16
            digital = 1
        else:
            for i in range(0, int(math.log10(setting.score)+1)):
                width += 16
                digital += 1
        score_image = pygame.Surface((width, 20)).convert_alpha()
        score_image.fill(transparent)
        score_image.set_alpha(self.alpha)
        for i in range(0, digital):
            n = int(setting.score%pow(10, i+1)/pow(10, i))
            score_image.blit(dead_screen_score_board_letter[n], (width-i*16-16, 0))
        self.image.blit(score_image, (215-width/2, 230))

    def print_best_score(self, setting):
        width = 0
        digital = 0
        if setting.best_score == 0:
            width = 16
            digital = 1
        else:
            for i in range(0, int(math.log10(setting.best_score)+1)):
                width += 16
                digital += 1
        score_image = pygame.Surface((width, 20)).convert_alpha()
        score_image.fill(transparent)
        score_image.set_alpha(self.alpha)
        for i in range(0, digital):
            n = int(setting.best_score%pow(10, i+1)/pow(10, i))
            score_image.blit(dead_screen_score_board_letter[n], (width-i*16-16, 0))
        self.image.blit(score_image, (215-width/2, 270))

    def restart_button_appear(self):
        restart_button_image = pygame.Surface((116, 70)).convert_alpha()
        restart_button_image.fill(transparent)
        restart_button_image.blit(dead_screen_restart_button, (0, 0))
        restart_button_image.set_alpha(self.alpha)
        self.image.blit(restart_button_image, (86, 330))