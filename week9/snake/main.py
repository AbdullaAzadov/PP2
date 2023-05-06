import pygame, random, time, sys

pygame.init()
scale = 2
# инициализируем константы

path = "C:/pp2/week9/snake/"
BLACK = (0, 4, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 600
WIDTH = 600
side_x = 0
side_y = 0
BLOCK_SIZE = 30
Field = [], []
lvl = 1
SCORE = 0
NEEDED = 5
start = time.time()
rgb_wall = (random.randint(33, 100), random.randint(33, 100), random.randint(33, 100))
rgb_snake = [252,133,29]
random.shuffle(rgb_snake)

lose = False

# спрайт яблока
apple = pygame.transform.scale(pygame.image.load(path+"apple.png"), (BLOCK_SIZE, BLOCK_SIZE))

# Шрифт и текст
font = pygame.font.Font(None, int(HEIGHT // 8))
gm_ovr = font.render("GAME OVER", 1, BLACK)
gm_ovr_rect = gm_ovr.get_rect()
gm_ovr_rect.center = (WIDTH / 2, HEIGHT / 2)
new_lvl = font.render("NEW LEVEL", 1, BLACK)
new_lvl_rect = new_lvl.get_rect()
new_lvl_rect.center = (WIDTH / 2, HEIGHT / 2)
deffont = pygame.font.Font(None, int(BLOCK_SIZE*1.5))

# Класс поинта
class Point:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

# при старте каждой игры будет определена рандомная позиция яблоки
food_x = random.randint(2, 7)
food_y = 10

# Класс стен (определение ректангла и рендер)
class Wall:
    def draw(self, x, y):
        rect = pygame.Rect(BLOCK_SIZE * x, BLOCK_SIZE * y, BLOCK_SIZE,
                           BLOCK_SIZE)
        pygame.draw.rect(SCREEN, rgb_wall, rect)

# Класс ябоки
class Food:
    # локация яблоки которая выдается раз в начале игры
    def __init__(self):
        self.location = (food_x, food_y)
    # рисуем
    def draw(self):
        global earned, food_x, food_y, start # earned- триггер который будет определять съел ли змея яблоку, и будущие позиции
        rect = pygame.Rect(BLOCK_SIZE * food_x, BLOCK_SIZE * food_y,
                           BLOCK_SIZE, BLOCK_SIZE)
        SCREEN.blit(apple, rect) # рендерим
        if earned or time.time() - start > 8: # если змея прикоснулась к яблоке
            while True:
                start = time.time()
                rand_x = random.randint(0, 19) # даем рандомное место и проверяем
                rand_y = random.randint(0, 19)
                if Field[rand_y][rand_x] == "=": # если все в порядке то, даем ранд значение к настоящим координатам
                    food_x, food_y = rand_x, rand_y
                    break
            earned = False # инача циклично будем пересоздавать яблоко, пока не определим подходящее место

# Класс игрока
class Snake:
    # координаты для появления в начале игры
    def __init__(self):
        self.body = [Point(random.randint(13, 18), 10)]
        self.dx = 0
        self.dy = 0
    # дельта х и у будут определять в куда перемещать змею
    def move(self):
        # Field - это мапа которая создана в тхт файле, служит чтобы находить столкновения
        # input - это некий лок который в игре не позволяет развернуться змее на 180 градусов зажатием 2 клавииш
        # lvl - каунтер уровня
        # lose - триггер отвечащий на то что игрок перешел границу или "съел" хвост
        global Field, input, lvl, earned, lose 
        for i in range(len(self.body) - 1, 0, -1):
            if self.body[0].x == self.body[i].x:
                if self.body[0].y == self.body[i].y: # если голова змеи равен с части тела то это означает проигрыщ
                    if not earned:
                        lose = True
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx # движение 
        self.body[0].y += self.dy
        # если змея будет выходить за границу, он не пропадет
        if self.body[0].x * BLOCK_SIZE > WIDTH: self.body[0].x = 0
        if self.body[0].y * BLOCK_SIZE > HEIGHT:self.body[0].y = 0
        if self.body[0].x < 0:  self.body[0].x = WIDTH / BLOCK_SIZE
        if self.body[0].y < 0:  self.body[0].y = HEIGHT / BLOCK_SIZE

        input = True
        # после движения, лок на инпут убираем
    def draw(self):
        point = self.body[0]
        # Рендерим его так чтобы отдельно голова была другого цвета
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y,
                           BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, rgb_snake, rect)

        for i, point in enumerate(self.body[1:]):
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y,
                               BLOCK_SIZE, BLOCK_SIZE)
            rgb = [rgb_snake[0] - 15 - (i * 3), rgb_snake[1] - 15 - (i * 3), rgb_snake[2] - 15 - (i * 3)]
            for ch in range(3): 
                if rgb[ch] < 0: rgb[ch] = 0
            pygame.draw.rect(SCREEN, rgb, rect)

        # Коллиззия
    def check_collision(self, food):
        global earned, SCORE
        location = (self.body[0].x, self.body[0].y)
        if location == (food_x, food_y):
            self.body.append(Point(food_x, food_y))
            earned = True
            SCORE+= 1
        # если голова змеи находиться на клетке что и еда, змея растет и earned становиться истиной, а также счетчик увеличывается

# Основной цикл
def main():
    global SCREEN, CLOCK, side_x, side_y, input, SCORE, earned, Field, lvl, lose, food_x, food_y, NEEDED, start, rgb_snake, rgb_wall
    # все эти глобалы нужны чтобы была возможность начинать заново игру без выхода из игры
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    
    # Сначала поле делаем пустым
    Field = [], []
    # открываем карту и делаем лист по строкам и закрываем файл
    with open(path + f'l{lvl-1}.txt') as f:
        lines = f.read().splitlines()
        Field = lines
    # Field - лист строк из файла по строкам
    earned = False
    input = True
    
    # Объявляем классы
    snake = Snake()
    food = Food()
    wall = Wall()

    # ОСновной цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # выход из игры
            # side - направления куда смотрит змея side_x = (-1 0 1), налево. не смотрит в бок. направо и также с y осью
            if event.type == pygame.KEYDOWN and input:
                if event.key == pygame.K_RIGHT and (side_x != -1):
                    snake.dx = 1
                    snake.dy = 0
                    side_x = 1
                    side_y = 0
                elif event.key == pygame.K_LEFT and (side_x != 1):
                    snake.dx = -1
                    snake.dy = 0
                    side_x = -1
                    side_y = 0
                elif event.key == pygame.K_UP and (side_y != 1):
                    snake.dx = 0
                    snake.dy = -1
                    side_y = -1
                    side_x = 0
                elif event.key == pygame.K_DOWN and (side_y != -1):
                    snake.dx = 0
                    snake.dy = 1
                    side_y = 1
                    side_x = 0
                input = False
        SCREEN.fill((rgb_wall[0] // 3, rgb_wall[1] // 3, rgb_wall[2] // 3))

        # запускаем классы и рендерим
        snake.check_collision(food)
        snake.move()        
        food.draw()
        snake.draw()

        # Если счет больше или равен чем нужно
        if (SCORE >= NEEDED):
            # настраиваем сколько нужно для след уровня и увеличываем уровень
            lvl += 1
            if lvl == 2:   NEEDED = 15
            elif lvl == 3: NEEDED = 30
            elif lvl == 4: NEEDED = 50
            else: NEEDED = 999

            # Cбрасываем все к новой карте и заново начинаем 
            start = time.time()
            earned = False
            input = False  
            lose = False
            snake = Snake()
            food = Food()
            wall = Wall() 
            food_x = random.randint(2, 7)
            food_y = 10 
            SCREEN.fill(rgb_wall)
            SCREEN.blit(new_lvl, new_lvl_rect)
            pygame.display.update()
            rgb_wall = (random.randint(33, 100), random.randint(33, 100), random.randint(33, 100))
            with open(path + f'l{lvl-1}.txt') as f:
                lines = f.read().splitlines()
                Field = lines
            time.sleep(1)
            continue
        # или иначе есди просто not earned, то проверяем столкнулся ли змея к стене с помошью пробежания циклом
        elif not earned:
            for y in range(0, len(Field)):
                for x in range(0, len(Field)):
                    if Field[y][x] == "#":
                        wall.draw(x, y)
                    if Field[snake.body[0].y][snake.body[0].x] == "#" or lose: # если он прикоснулся к стене или есть триггер lose
                        SCREEN.fill(rgb_wall)
                        SCREEN.blit(gm_ovr, gm_ovr_rect)
                        pygame.display.update()
                        time.sleep(1)
                        lvl = 1
                        start = time.time()
                        SCORE = 0
                        NEEDED = 5
                        rgb_snake = [252,133,29]
                        random.shuffle(rgb_snake)   
                        # Выводим game over скрин и перезапускаем все
                        with open(path + f'l{lvl-1}.txt') as f:
                            lines = f.read().splitlines()
                            Field = lines
                        earned = False
                        input = True  
                        snake = Snake()
                        food = Food()
                        wall = Wall()
                        food_x = random.randint(2, 7)
                        food_y = 10 
                        rgb_wall = (random.randint(33, 100), random.randint(33, 100), random.randint(33, 100))
                        lose = False
                        continue
        # Рендер текста на экране
        if lvl != 5: scr = deffont.render("SCORE: " + str(SCORE) + "/" + str(NEEDED) , 1, BLACK)
        else: scr = deffont.render("SCORE: " + str(SCORE), 1, BLACK)
        SCREEN.blit(scr, (20,1))

        l_txt = deffont.render("LEVEL: " + str(lvl) + "/5" , 1, BLACK)
        l_rect = l_txt.get_rect()
        l_rect.right = WIDTH - 20
        SCREEN.blit(l_txt, l_rect)

        pygame.display.update()
        # скорость игры регилируется с помошью лимита на фпс. скорость змеи растет с каждым новым уровнем
        speed = 5 + lvl-1
        if speed > 8: speed = 8
        CLOCK.tick(speed)

main()
