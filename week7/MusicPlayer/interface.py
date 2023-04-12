import pygame
from settings import *

#   Конпки

# Пауза
btn_pause = pygame.transform.scale(pygame.image.load(dir + "pause.png"), (controlbar_rect.h * 0.8))
btn_pause_rect = btn_pause.get_rect()
btn_pause_rect.centerx, btn_pause_rect.centery = controlbar_rect.centerx, controlbar_rect.centery
# Старт
btn_play = pygame.transform.scale(pygame.image.load(dir + "play.png"), (controlbar_rect.h * 0.8)) 
btn_play_rect = btn_play.get_rect()
btn_play_rect.centerx, btn_play_rect.centery = controlbar_rect.centerx, controlbar_rect.centery
