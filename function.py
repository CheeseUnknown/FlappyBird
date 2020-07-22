import pygame, sys
from pygame.locals import *
from setting.setting import *

def get_event(setting, mouse_position, main_screen):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit(0)
        if event.type == MOUSEBUTTONUP:
            if setting.phase == 0:
                if mouse_position[0] >=86 and mouse_position[0] <= 202 and mouse_position[1] >= 300 and mouse_position[1] <= 370:
                    setting.phase = 1
            elif setting.phase == 2:
                main_screen.gaming_screen.bird_groupSingle.sprite.velocity = -3
                fly_sound.play()
            elif setting.phase == 3:
                if mouse_position[0] >= 86 and mouse_position[0] <= 202 and mouse_position[1] >= 330 and mouse_position[1] <= 400 and main_screen.dead_screen.alpha >= 255:
                    setting.score = 0
                    main_screen.dead_screen.alpha = 0
                    main_screen.gaming_screen.load()
                    setting.phase = 1
        if event.type == MOUSEBUTTONDOWN:
            if setting.phase == 1:
                setting.phase = 2

def write_txt(setting):
    with open("setting/setting.txt", "r") as f:
        lines = f.readlines()
    with open('setting/setting.txt', "w") as f:
        for line in lines:
            if "bestscore:" in line:
                line = "bestscore:" + str(setting.best_score)
            f.write(line)