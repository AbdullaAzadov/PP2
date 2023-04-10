import pygame
import datetime

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 720
fps = pygame.time.Clock()
pygame.display.set_caption("Mickey Mouse Clock")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
path = r"C:/pp2/week7/lab 7 - mickey clock/" 

background = pygame.image.load(path + "clock.png")
arrow_small = pygame.image.load(path + "arrow_s.png")
arrow_big = pygame.image.load(path + "arrow_b.png")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
                
    screen.blit(background, (0, 0))
    
    pygame.display.flip()
    fps.tick(60)