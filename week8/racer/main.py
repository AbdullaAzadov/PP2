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
BLUE  = (0, 0, 224)
RED   = (127, 0, 0)
BLACK = (30, 30, 30)
WHITE = (255, 255, 255)
 
# Разрешение экрана и настройки
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COIN = 0
spawn_coin = False
collected = False 

# Создаем окно игры
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# Шрифты:
smallfont = pygame.font.Font(None, 36)
bigfont = pygame.font.Font(None, int(SCREEN_HEIGHT / 10))
game_over = bigfont.render("GAME OVER", 1, BLACK)
game_over_rect = game_over.get_rect()
game_over_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

# Фоновая музыка. Если музыка заканчивется, есть событие который перезапускает музыку
pygame.mixer.music.load(path + "background.wav")
pygame.mixer.music.play()
END_TRACK = pygame.USEREVENT + 2
pygame.mixer.music.set_endevent(END_TRACK)

# Фон и значки интерфейса
background = pygame.image.load(path + "AnimatedStreet.png")
coinlogo = pygame.image.load(path + "coinlogo.png")
coinlogo_rect = coinlogo.get_rect()
coinlogo_rect.right = SCREEN_WIDTH-5

# Классы
#   класс врага. Инициализация и объявление
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        global SCORE, SPEED
        # Если враг за границей экрана то спавним его заново и увеличиваем скорость и счет
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE+= 1
            # Максимальная скорость в игре 20. Так как после 20 становится не возможно играть
            if SPEED < 20:
                SPEED+= 0.5
# Класс коина. можно сказать что оно унаследовано у Enemy
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24,SCREEN_WIDTH-24), 0)    
        # Также инициализируем
      def move(self):
        global spawn_coin, collected
        # Спавн_коин это триггер, если она истина то коин может быть заспавнена.
        # Collected это тоже триггер, если она активна то значит что игрок взял этот коин
        self.rect.move_ip(0,SPEED//2)# Коин будет двигаться чуть медленнее
        if (self.rect.top > SCREEN_HEIGHT) and spawn_coin:
            self.rect.top = 0
            self.rect.center = (random.randint(24, 384), 0)
            spawn_coin = False # После спауна объязательно спаун отключаем.
        if collected:
            self.rect.top = SCREEN_HEIGHT+1
            collected = False

            

# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        # Такая же процедура что и с пред.
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  # в сотвесттвии с инпутом, машина передвигается
 
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группировка спрайтов
# делаем группировку как собирамые вещи и туда добавляем коин
collectable = pygame.sprite.Group()
collectable.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
# Добавляем событие с коином. каждые 4 секунд триггер для коина будет активен
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 4000)

 
# Главный игровой цикл
while True:
    # Ивенты
    for event in pygame.event.get():
        if event.type == COIN_SPAWN:
            spawn_coin = True
        # Проверяем если произошел ивент END_TRACK заново запускаем музыку
        if event.type == END_TRACK:
            pygame.mixer.music.load(path + "background.wav")
            pygame.mixer.music.play()
        # Выход из игры
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.blit(background, (0, 0))

    #Движение и рендеринг спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for entity in collectable:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    # рендер счета
    score = smallfont.render(" " + str(SCORE), 1, BLUE)
    DISPLAYSURF.blit(score, (5, 5))
    DISPLAYSURF.blit(coinlogo, coinlogo_rect)
    cn = smallfont.render(str(COIN), 1, (170, 131, 24))
    cn_rect = cn.get_rect()
    cn_rect.right = coinlogo_rect.left
    cn_rect.centery = coinlogo_rect.centery
    DISPLAYSURF.blit(cn, cn_rect)


    #Коллизия и столкновения
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.mixer.Sound(path + 'crash.wav').play()
          DISPLAYSURF.blit(game_over, game_over_rect)
          time.sleep(0.5)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    if pygame.sprite.spritecollideany(P1, collectable):
        pygame.mixer.Sound(path + "coin.ogg").play()
        collected = True
        COIN+= 1
         
    pygame.display.update()
    FramePerSec.tick(FPS)
