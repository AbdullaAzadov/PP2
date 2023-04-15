from os import scandir
from select import select
import pygame, random, time

pygame.init()

BLACK = (0, 4, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
side_x = 0
side_y = 0
BLOCK_SIZE = 20
earned = False
input = True

path = "C:/pp2/week8/snake/"
font = pygame.font.Font(None, int(HEIGHT // 8))
gm_ovr = font.render("GAME OVER", 1, BLACK)
gm_ovr_rect = gm_ovr.get_rect()
gm_ovr_rect.center = (WIDTH / 2, HEIGHT / 2)

Field = [], []
with open(path + 'l0.txt') as f:
    lines = f.read().splitlines()
    Field = lines


class Point:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


food_x = 10
food_y = 10


class Wall:

    def __init__(self):
        pass

    def draw(self, x, y):
        rect = pygame.Rect(BLOCK_SIZE * x, BLOCK_SIZE * y, BLOCK_SIZE,
                           BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 100, 0), rect)


class Food:

    def __init__(self):
        self.location = (food_x, food_y)

    def draw(self):
        global earned, food_x, food_y
        rect = pygame.Rect(BLOCK_SIZE * food_x, BLOCK_SIZE * food_y,
                           BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 0, 255), rect)
        if earned:
            while True:
                rand_x = random.randint(0, 19)
                rand_y = random.randint(0, 19)
                if Field[rand_y][rand_x] == "=":
                    food_x, food_y = rand_x, rand_y
                    break
            earned = False


class Snake:

    def __init__(self):
        self.body = [Point(random.randint(1, 19), random.randint(1, 19))]
        self.dx = 0
        self.dy = 0

    def move(self):
        global Field, input
        for i in range(len(self.body) - 1, 0, -1):
            if self.body[0].x == self.body[i].x:
                if self.body[0].y == self.body[i].y:
                    if not earned:
                        SCREEN.fill((200, 0, 0))
                        SCREEN.blit(gm_ovr, gm_ovr_rect)
                        pygame.display.update()
                        time.sleep(2)
                        pygame.quit()
                        sys.exit()
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0

        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE

        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE
        input = True
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y,
                           BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y,
                               BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        global earned
        location = (self.body[0].x, self.body[0].y)
        if location == (food_x, food_y):
            self.body.append(Point(food_x, food_y))
            earned = True


def main():
    global SCREEN, CLOCK, side_x, side_y, input
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    snake = Snake()
    food = Food()
    wall = Wall()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        SCREEN.fill(BLACK)

        snake.check_collision(food)
        snake.move()

        food.draw()
        snake.draw()
        for y in range(0, len(Field)):
            for x in range(0, len(Field)):
                if Field[y][x] == "#":
                    wall.draw(x, y)
                if Field[snake.body[0].y][snake.body[0].x] == "#":
                    SCREEN.fill((200, 0, 0))
                    SCREEN.blit(gm_ovr, gm_ovr_rect)
                    pygame.display.update()
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()

        #drawGrid()
        pygame.display.update()
        CLOCK.tick(5)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            #pygame.draw.rect(SCREEN, LINE_COLOR, rect)


main()
