import pygame, sys
from pygame.locals import *
from setting.setting import *
from function import *
from screen.mainScreen import *

pygame.init()
FPS_control = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
main_screen = MainScreen()
setting = Setting()

while True:
    ticks = pygame.time.get_ticks()
    mouse_position = pygame.mouse.get_pos()
    get_event(setting, mouse_position, main_screen)

    main_screen.update(ticks, setting)

    main_screen.draw(screen, setting)
    
    FPS_control.tick(FPS)
    pygame.display.update()