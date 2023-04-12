import pygame, random, os
from settings import *
from interface import *

# Инициализация
pygame.init()
pygame.mixer.init()

# Функции
def releasedButton(key, act0, act1): 
    return act0[key] and not act1[key]

def changeMusic(cntr, isN, len, dir, music, r_mode, l_mode):
    if not r_mode and not l_mode:  cntr = (cntr + 1 - (2*isN)) % len
    elif not l_mode:
        while 1:
            tmp = random.randint(0, len-1)
            if tmp != cntr:
                cntr = tmp
                break

    pygame.mixer.music.load(dir + "music/" + music[cntr])
    pygame.mixer.music.play()
    return cntr

# Игровой цикл
launched = True
while launched:
    action = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    # Механика
    # Пред/След    
    if releasedButton(pygame.K_RIGHT, action, prev_action): 
        music_cntr = changeMusic(music_cntr, 0, len(music), dir, music, randomOn, loop)  
    if releasedButton(pygame.K_LEFT, action, prev_action): 
        music_cntr = changeMusic(music_cntr, 1, len(music), dir, music, randomOn, loop)
    # Пауза/Старт
    if releasedButton(pygame.K_SPACE, action, prev_action) and not pause: 
        pygame.mixer.music.pause()
        pause = not pause
    elif releasedButton(pygame.K_SPACE, action, prev_action) and pause:
        pygame.mixer.music.unpause()
        pause = not pause

    # Режим перемещивание песен
    if releasedButton(pygame.K_r, action, prev_action): randomOn = not randomOn
    # Режим повтора
    if releasedButton(pygame.K_l, action, prev_action): loop = not loop

    print(music_cntr)

    screen.fill(bg_clr) 
    controlbar.fill(bar_bg_clr)
    controlbar.blit(btn_pause, btn_pause_rect)
    screen.blit(controlbar, (0, height - controlbar.get_height()))
    
    prev_action = action
    pygame.display.flip()
    fps.tick(60)