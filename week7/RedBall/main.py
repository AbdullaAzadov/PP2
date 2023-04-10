import pygame

pygame.init()

width = 1280
height = 720
fps = pygame.time.Clock()
pygame.display.set_caption("Red Ball")
screen = pygame.display.set_mode((width, height))

ball = pygame.Surface((50, 50))
ball_x = width / 2 - 25
ball_y = height / 2 - 25

def controller(pressed, x, y, sc_x, sc_y):
    if pressed[pygame.K_RIGHT]:
        if x + 70 >= sc_x: x = sc_x - 50
        else: x+= 20
    if pressed[pygame.K_LEFT]:
        if x - 20 <= 0: x = 0
        else: x-= 20
    if pressed[pygame.K_UP]:
        if y - 20 <= 0: y = 0
        else: y-= 20
    if pressed[pygame.K_DOWN]:
        if y + 70 >= sc_y: y = sc_y - 50
        else: y+= 20   
    return x, y 

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    ball_x, ball_y = controller(pygame.key.get_pressed(), ball_x, ball_y, width, height)    

    ball.fill((224, 224, 224))
    screen.fill((224, 224, 224))

    pygame.draw.circle(ball, (224, 0, 0), (25, 25), 25)
    screen.blit(ball, (ball_x, ball_y))
    
    pygame.display.flip()
    fps.tick(60)