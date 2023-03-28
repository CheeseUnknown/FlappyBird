import pygame, datetime
from pygame.locals import *
from setting.setting import *
from screen.readyScreen import *
from screen.beginningScreen import *
from screen.gamingScreen import *
from screen.deadScreen import *

class MainScreen(object):
    def __init__(self):
        self.load()

    def load_image(self, time):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        #choose the day or night background according to the time
        if time>=6 and time<=18:
            self.image.blit(main_screen_background_day, (0, 0))
        elif time<6 or time>18:
            self.image.blit(main_screen_background_night, (0, 0))
        self.image.blit(main_screen_land, (self.land_x, 400))

    def load(self):
        self.time = datetime.datetime.now().hour
        self.land_x = 0
        self.load_image(self.time)
        self.ready_screen = ReadyScreen()
        self.beginning_screen = BeginningScreen()
        self.gaming_screen = GamingScreen()
        self.dead_screen = DeadScreen()
        self.x = 0
        self.y = 0

    def update(self, ticks, setting):
        self.load_image(self.time)
        self.land_move(setting)
        if setting.phase == 0:
            self.ready_screen.update(ticks)
        elif setting.phase == 1:
            self.beginning_screen.update(ticks)
        elif setting.phase == 2:
            self.gaming_screen.update(ticks, setting, self.dead_screen)
        elif setting.phase == 3:
            self.dead_screen.update()

    def draw(self, screen, setting):
        if setting.phase == 0:
            self.ready_screen.draw(self.image)
        elif setting.phase == 1:
            self.beginning_screen.draw(self.image)
        elif setting.phase == 2:
            self.gaming_screen.draw(self.image, setting)
        elif setting.phase == 3:
            self.gaming_screen.draw(self.image, setting)#keep the background
            self.dead_screen.draw(self.image, setting)
        screen.blit(self.image, (self.x, self.y))

    def land_move(self, setting):
        if setting.phase != 3:
            self.land_x -= 1
            if self.land_x <= -48:
                self.land_x = 0