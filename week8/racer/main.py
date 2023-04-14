import pygame, sys
from pygame.locals import *
import random, time
 
# Инициализация и настройка пути к ассетам 
pygame.init()
pygame.mixer.init()
play = True
path = "C:/pp2/week8/racer/"

# Ставим ограничение кадров
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Разрешение экрана и настройка скорости
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 4
 
# Создаем окно игры
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
# Шрифты:
smallfont = pygame.font.Font(None, int(SCREEN_HEIGHT / 20))
bigfont = pygame.font.Font(None, int(SCREEN_HEIGHT / 15))

# Фоновая музыка
pygame.mixer.music.load(path + "background.wav")
pygame.mixer.music.play()
END_TRACK = pygame.USEREVENT + 2
pygame.mixer.music.set_endevent(END_TRACK)


# Классы
#   класс врага 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
P1 = Player()
E1 = Enemy()
 
# Группировка спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
 
# Главный игровой цикл
while True:
    # Ивенты
    for event in pygame.event.get():
        # Проверяем если произошел ивент END_TRACK заново запускаем музыку
        if event.type == END_TRACK:
            pygame.mixer.music.load(path + "background.wav")
            pygame.mixer.music.play()
        # Выход из игры
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.fill(WHITE)
 
    #Движение и рендеринг спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #Коллизия и столкновения
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
