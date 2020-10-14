import pygame
import random
import sys
import os
import time

pygame.init() ##включает графику и звуки

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' ## окно открывается в точке 0,0 (левый верхний угол)
#os.environ['SDL_VIDEO_CENTERED'] = '1' ##окно открывается по середине
info = pygame.display.Info() ##получение разрешения монитора
WIDTH_WIN, HEIGHT_WIN = info.current_w * 100 // 125, info.current_h * 100 // 125  ##расширение окна
print(info.current_w, info.current_h)
print(WIDTH_WIN, HEIGHT_WIN)S

screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN)) ##переменная окна
pygame.mouse.set_visible(False) ## видимость мыши на экране (невидна)

FPS = 60 ## частота смены кадров в секунду
clock = pygame.time.Clock() 

run = True
while run: 
    for e in pygame.event.get(): ## в е попадают любые изменения/нажатия на клаве или мыши
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    ## pygame.QUIT нажатие на крестик закрытия окна
    ## e.tipe == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: нажата клавиша escape 