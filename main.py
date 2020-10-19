import pygame
import random
import sys
import os
import time
from colors import COLOR

pygame.init() ##включает графику и звуки

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30' ## окно открывается в точке 0,0 (левый верхний угол)
#os.environ['SDL_VIDEO_CENTERED'] = '1' ##окно открывается по середине
info = pygame.display.Info() ##получение разрешения монитора
WIDTH_WIN, HEIGHT_WIN = info.current_w * 100 // 100, info.current_h * 100 //100  ##расширение окна
##print(info.current_w, info.current_h)
##print(WIDTH_WIN, HEIGHT_WIN)

path = os.path.dirname(os.path.abspath(__file__)) ## поиск пути к файлу

saturn = os.path.join(path, '6s.png') ## присваиваем переменной картинку
pygame.display.set_icon(pygame.image.load(saturn)) ##взятие изображения на иконку
pygame.display.set_caption('Stars') ## имя для открывшегося окна
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN)) ## создание окна по размерам(переменная окна. две скобки т.к. это картеж )
pygame.mouse.set_visible(False) ## видимость мыши на экране (невидна)

FPS = 450 ## частота смены кадров в секунду
clock = pygame.time.Clock() 
NUMBER_OF_STARS = 300
NIGHT_BG_COLOR = (5,0,50)
p = " " * (WIDTH_WIN //2 //4)

class Stars(pygame.sprite.Sprite):  ## создание спрайта "звезда"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = random.randint(1, 2) ##ставим скорость, размер, положение на экране
        self.size = random.randint(1, 3)
        self.pos = random.randrange(WIDTH_WIN), random.randrange(HEIGHT_WIN)
        self.image = pygame.Surface((self.size *2, self.size *2)) ## рамка вокруг изображения и рисование круга (звезды) в зтой области
        pygame.draw.circle(self.image,pygame.Color(
            random.choice(COLOR[238:262])), [self.size, self.size], self.size)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = WIDTH_WIN



class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load(os.path.join(path,'6s.png'))
        self.image =self.image_orig.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.rot = 0
        self.angel = 0.5

    def update(self):
        self.rot = (self.rot + self.angel) % 360
        self.image = pygame.transform.rotate(self.image_orig, self.rot)
        ##self.image = pygame.transform.squre(5,5)
        self.rect = self.image.get_rect(center=self.rect.center)

sprites = pygame.sprite.LayeredUpdates() ##создание массива (списка). LayeredUpdates - группа позволяющая перемещать спрайты по слоям
for _ in range(NUMBER_OF_STARS): 
    stars = Stars()
    sprites.add(stars, layer=0) ## доюавляем к списку каждую звезду

pl = Planet(WIDTH_WIN // 4, HEIGHT_WIN // 2)
sprites.add(pl,layer = 0)

run = True
while run: 
    clock.tick(FPS)
    for e in pygame.event.get(): ## в е попадают любые изменения/нажатия на клаве или мыши
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    ## pygame.QUIT нажатие на крестик закрытия окна
    ## e.tipe == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: нажата клавиша escape 
    sprites.update()
    screen.fill(NIGHT_BG_COLOR) ## заливка фона цветом с переменной
    sprites.draw(screen)
    pygame.display.update()
    pygame.display.set_caption(f'Stars{p}FPS: {int(clock.get_fps())}')





