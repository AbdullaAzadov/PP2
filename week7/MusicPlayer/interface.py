import pygame
from settings import *

#   Конпки

# Пауза/Cтарт
btn_pause = pygame.transform.scale(pygame.image.load(dir + "pause.png"), (controlbar_rect.h/2, controlbar_rect.h/2))
btn_play = pygame.transform.scale(pygame.image.load(dir + "play.png"), (controlbar_rect.h/2, controlbar_rect.h/2)) 
btn_pause_rect = btn_pause.get_rect()
btn_pause_rect.centerx, btn_pause_rect.centery = controlbar_rect.centerx, controlbar_rect.centery
# Пред/Cлед
btn_next = pygame.transform.scale(pygame.image.load(dir + "next.png"), (controlbar_rect.h/3, controlbar_rect.h/3))
btn_prev = pygame.transform.scale(pygame.image.load(dir + "prev.png"), (controlbar_rect.h/3, controlbar_rect.h/3)) 
btn_next_rect = btn_next.get_rect()
btn_next_rect.centerx, btn_next_rect.centery = controlbar_rect.centerx + btn_pause_rect.w, controlbar_rect.centery
btn_prev_rect = btn_prev.get_rect()
btn_prev_rect.centerx, btn_prev_rect.centery = controlbar_rect.centerx - btn_pause_rect.w, controlbar_rect.centery
# повтор
btn_loopOff = pygame.transform.scale(pygame.image.load(dir + "loop0.png"), (controlbar_rect.h/8, controlbar_rect.h/8)) 
btn_loopOn = pygame.transform.scale(pygame.image.load(dir + "loop1.png"), (controlbar_rect.h/8, controlbar_rect.h/8)) 
btn_loop_rect = btn_loopOff.get_rect()
btn_loop_rect.centerx, btn_loop_rect.centery = controlbar_rect.centerx - btn_pause_rect.w - btn_next_rect.w , controlbar_rect.centery
# случайная песня
btn_randOff = pygame.transform.scale(pygame.image.load(dir + "rand0.png"), (controlbar_rect.h/8, controlbar_rect.h/8)) 
btn_randOn = pygame.transform.scale(pygame.image.load(dir + "rand1.png"), (controlbar_rect.h/8, controlbar_rect.h/8)) 
btn_rand_rect = btn_randOff.get_rect()
btn_rand_rect.centerx, btn_rand_rect.centery = controlbar_rect.centerx + btn_pause_rect.w + btn_next_rect.w , controlbar_rect.centery
# иконка музыки
emptyPic = pygame.transform.scale(pygame.image.load(dir + "song.png"), (songPicture_rect.h/2, songPicture_rect.h/2))
emptyPic_copy = emptyPic
emptyPic_rect = emptyPic.get_rect()
emptyPic_rect.right, emptyPic_rect.bottom = width / 2, height / 3