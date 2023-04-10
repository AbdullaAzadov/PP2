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
arrow_m = pygame.image.load(path + "arrow_b.png")
arrow_s = pygame.image.load(path + "arrow_s.png")
plane = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

arrow_sbox = arrow_s.get_rect()
arrow_sc = arrow_s
arrow_mbox = arrow_m.get_rect()
arrow_mc = arrow_m

def rotate(image, angle, rect):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    current = datetime.datetime.now()
    angle_s = int(current.second) * -6
    arrow_s, arrow_sbox = rotate(arrow_sc, angle_s, arrow_sbox)
    
    angle_m = int(current.minute) * -6
    arrow_m, arrow_mbox = rotate(arrow_mc, angle_m, arrow_mbox)
    

    plane.blit(background, (0, 0))
    plane.blit(arrow_s, arrow_sbox)
    plane.blit(arrow_m, arrow_mbox)
    screen.blit(plane, (0, 0))
    

    pygame.display.flip()
    fps.tick(60)