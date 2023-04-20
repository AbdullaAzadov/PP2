import pygame, sys
from pygame.locals import *
import random, time
 
# Инициализация и настройка пути к ассетам 
pygame.init()
pygame.mixer.init()
play = True
path = "C:/pp2/week9/racer/"

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
# Создаем некий буст к скорости который будет увеличиваться, когда мы собираем монеты
BOOST = 0
SCORE = 0
COIN = 0
# Триггеры спавна монет и триггеры взятия монет
spawn_coin = False
spawn_bigcoin = False
spawn_diamond = False
coin_collected = False 
bigcoin_collected = False
diamond_collected = False

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
        self.rect.move_ip(0,SPEED + BOOST)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE+= 1
            # Максимальная скорость в игре 20. Так как после 20 становится не возможно играть
            if SPEED < 20:
                SPEED+= 0.25
# Класс коина. можно сказать что оно унаследовано у Enemy
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24,SCREEN_WIDTH-24), 0)    
        # Также инициализируем
      def move(self):
        global spawn_coin, coin_collected
        # Спавн_коин это триггер, если она истина то коин может быть заспавнена.
        # coin_collected это тоже триггер, если она активна то значит что игрок взял этот коин
        self.rect.move_ip(0,SPEED / 3)# Коин будет двигаться чуть медленнее
        if (self.rect.top > SCREEN_HEIGHT) and spawn_coin:
            self.rect.top = -50
            self.rect.center = (random.randint(24, 384), 0)
            spawn_coin = False # После спауна объязательно спаун отключаем.
        if coin_collected:
            self.rect.top = SCREEN_HEIGHT+1
            coin_collected = False
# Точно такой же коин (см. сверху), но с другими размерами и скоростями
class BigCoin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "bigcoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32,SCREEN_WIDTH-32), 0)    
      def move(self):
        global spawn_bigcoin, bigcoin_collected
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT) and spawn_bigcoin:
            self.rect.top = -100
            self.rect.center = (random.randint(32, 368), 0)
            spawn_bigcoin = False 
        if bigcoin_collected:
            self.rect.top = SCREEN_HEIGHT+1
            bigcoin_collected = False     

class Diamond(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "diamond.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(16,SCREEN_WIDTH-16), 0)    
      def move(self):
        global spawn_diamond, diamond_collected
        self.rect.move_ip(0, SPEED *(0,67))
        if (self.rect.top > SCREEN_HEIGHT) and spawn_diamond:
            self.rect.top = -100
            self.rect.center = (random.randint(16, 384), 0)
            spawn_diamond = False
        if diamond_collected:
            self.rect.top = SCREEN_HEIGHT+1
            diamond_collected = False     


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
# Объявляем классы
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = BigCoin()
C3 = Diamond()

# Группировка спрайтов
coin = pygame.sprite.Group()
coin.add(C1)
bigcoin = pygame.sprite.Group()
bigcoin.add(C2)
diamond = pygame.sprite.Group()
diamond.add(C3)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)
 
# Добавляем событие с коином. каждые 6, 11, 17 секунд триггер для определенных коинов станет активен
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 6000)
BIGCOIN_SPAWN = pygame.USEREVENT + 3
pygame.time.set_timer(BIGCOIN_SPAWN, 11000)
DIAMOND_SPAWN = pygame.USEREVENT + 4
pygame.time.set_timer(DIAMOND_SPAWN, 17000)
# Главный игровой цикл
while True:
    # Ивенты
    for event in pygame.event.get():
        if event.type == COIN_SPAWN:
            spawn_coin = True
        if event.type == BIGCOIN_SPAWN:
            spawn_bigcoin = True
        if event.type == DIAMOND_SPAWN:
            spawn_diamond = True
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
    if pygame.sprite.spritecollideany(P1, coin):
        pygame.mixer.Sound(path + "coin.ogg").play()
        coin_collected = True
        COIN+= 1
    if pygame.sprite.spritecollideany(P1, bigcoin):
        pygame.mixer.Sound(path + "coin.ogg").play()
        bigcoin_collected = True
        COIN+= 3
    if pygame.sprite.spritecollideany(P1, diamond):
        pygame.mixer.Sound(path + "coin.ogg").play()
        diamond_collected = True
        COIN+= 5

    BOOST = COIN // 5
    print(SPEED + BOOST)
    pygame.display.update()
    FramePerSec.tick(FPS)
