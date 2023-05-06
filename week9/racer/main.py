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
SPEED = 2.5
PlayerSpeed = SPEED
# Создаем некий буст к скорости который будет увеличиваться, когда мы собираем монеты
BOOST = .5
SCORE = 0
COIN = 0
# Триггеры спавна монет
spawn_coin = False
spawn_bigcoin = False
spawn_diamond = False

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
        self.image = pygame.image.load(path + f"Enemy{random.randint(0, 5)}.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(10, SCREEN_WIDTH - 10 - self.rect.w), random.randint(-5*self.rect.h, -2*self.rect.h)
 
      def move(self, respawn):
        global SCORE, SPEED
        # Если враг за границей экрана то спавним его заново и увеличиваем скорость и счет
        self.rect.move_ip(0,SPEED + BOOST)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE+= 1
            SPEED+= 0.1
        if self.rect.top > SCREEN_HEIGHT or respawn:
            self.rect.left, self.rect.bottom = random.randint(10, SCREEN_WIDTH - 10 - self.rect.w), random.randint(-5*self.rect.h, -2*self.rect.h)


class Background(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "AnimatedStreet.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = 0, 0
 
      def move(self):
        global SPEED
        # Если враг за границей экрана то спавним его заново и увеличиваем скорость и счет
        self.rect.move_ip(0,SPEED)
        if (self.rect.centery >= SCREEN_HEIGHT):
            self.rect.centery = 0

# Класс коина. можно сказать что оно унаследовано у Enemy
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24,SCREEN_WIDTH-24), -self.rect.h)    
        # Также инициализируем
        
      def move(self, collect):
        global spawn_coin, BOOST, COIN
        # Спавн_коин это триггер, если она истина то коин может быть заспавнена.
        # collect это тоже триггер, если она активна то значит что игрок взял этот коин
        self.rect.move_ip(0,SPEED)# Коин будет двигаться чуть медленнее
        if (self.rect.top > SCREEN_HEIGHT) and spawn_coin:
            self.rect.top = -50
            self.rect.center = (random.randint(24, 384), -self.rect.h)
            spawn_coin = False # После спауна объязательно спаун отключаем.
        if collect:
            self.rect.top = SCREEN_HEIGHT+1
            COIN+= 1
            BOOST+= 0.1

# Точно такой же коин (см. сверху), но с другими размерами и скоростями
class BigCoin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "bigcoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32,SCREEN_WIDTH-32), -self.rect.h)    
      def move(self, collect):
        global spawn_bigcoin, BOOST, COIN
        if spawn_bigcoin:
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > SCREEN_HEIGHT) and spawn_bigcoin:
                self.rect.top = -100
                self.rect.center = (random.randint(32, 368), -self.rect.h)
                spawn_bigcoin = False 
            if collect:
                self.rect.top = SCREEN_HEIGHT+1
                COIN+= 2
                BOOST+= 0.175

class Diamond(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + "diamond.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(16,SCREEN_WIDTH-16), -self.rect.h)    

      def move(self, collect):
        global spawn_diamond, BOOST, COIN
        if spawn_diamond:
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > SCREEN_HEIGHT) and spawn_diamond:
                self.rect.top = -100
                self.rect.center = (random.randint(16, 384), -self.rect.h)
                spawn_diamond = False
            if collect:
                BOOST+= 0.25
                COIN+= 3
                self.rect.top = SCREEN_HEIGHT+1
                   


# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path + f"Player{random.randint(0, 2)}.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        # Такая же процедура что и с пред.
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-PlayerSpeed, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(PlayerSpeed, 0)
        if self.rect.top > 0:
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -PlayerSpeed)
        if self.rect.bottom < SCREEN_HEIGHT:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, PlayerSpeed)
                  # в сотвесттвии с инпутом, машина передвигается
# Объявляем классы
P1 = Player()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
E4 = Enemy()
C1 = Coin()
C2 = BigCoin()
C3 = Diamond()
BG = Background()

# Группировка спрайтов
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
coins.add(C3)

enemies = pygame.sprite.Group()
enemies.add(E1)

entity = pygame.sprite.Group()
entity.add(BG)
entity.add(P1)

 
# Добавляем событие с коином. каждые 6, 11, 17 секунд триггер для определенных коинов станет активен
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 6000)
BIGCOIN_SPAWN = pygame.USEREVENT + 3
pygame.time.set_timer(BIGCOIN_SPAWN, 11000)
DIAMOND_SPAWN = pygame.USEREVENT + 4
pygame.time.set_timer(DIAMOND_SPAWN, 17000)
# Главный игровой цикл
while True:
    PlayerSpeed = SPEED
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
 
 

    #Движение и рендеринг спрайтов
    for ent in entity:
        DISPLAYSURF.blit(ent.image, ent.rect)
        ent.move()
    for e in enemies:
        DISPLAYSURF.blit(e.image, e.rect)
        e.move(False)
    for c in coins:
        DISPLAYSURF.blit(c.image, c.rect)
        c.move(False)
        
    # рендер счета
    score = smallfont.render(" " + str(SCORE), 1, BLUE)
    DISPLAYSURF.blit(score, (5, 5))
    DISPLAYSURF.blit(coinlogo, coinlogo_rect)
    cn = smallfont.render(str(COIN), 1, (170, 131, 24))
    cn_rect = cn.get_rect()
    cn_rect.right = coinlogo_rect.left
    cn_rect.centery = coinlogo_rect.centery
    DISPLAYSURF.blit(cn, cn_rect)

    if 5 <= COIN < 10 : enemies.add(E2)
    if 15 <= COIN < 25: enemies.add(E3)
    if 30 <= COIN     : enemies.add(E4)

    #Коллизия и столкновения
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.mixer.Sound(path + 'crash.wav').play()
          DISPLAYSURF.blit(game_over, game_over_rect)
          pygame.display.update()
          time.sleep(1)
          pygame.quit()
          sys.exit()

    for c in coins:
        if pygame.sprite.collide_rect(P1, c):
            pygame.mixer.Sound(path + "coin.ogg").play()
            c.move(True)


    for c in enemies:
        for i in enemies:
            if pygame.sprite.collide_rect(c, i) and c != i:
                c.move(True)

    if SPEED > 5: SPEED = 5
    if BOOST > 10: BOOST = 10
    print(SPEED + BOOST)
    pygame.display.update()
    pygame.display.set_caption(str(FramePerSec))
    FramePerSec.tick(FPS)
