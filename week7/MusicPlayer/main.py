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

def mouseinRange(mouse, l, r, u, d):
    if l <= mouse[0] <= r and u <= mouse[1] <= d: return True
    else: return False

def rotate(image, angle, rect):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


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

# Взаимодействие с кнопками
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # нажатие на паузу
    if releasedButton(0, click, prev_click) and mouseinRange(mouse, btn_pause_rect.left, btn_pause_rect.right, btn_pause_rect.top, btn_pause_rect.bottom + controlbar_up):
            if not pause: pygame.mixer.music.pause()
            else: pygame.mixer.music.unpause()
            pause = not pause
    # нажатие на след/пред
    if releasedButton(0, click, prev_click) and mouseinRange(mouse, btn_prev_rect.left, btn_prev_rect.right, btn_prev_rect.top + controlbar_up, btn_prev_rect.bottom + controlbar_up):
        music_cntr = changeMusic(music_cntr, 1, len(music), dir, music, randomOn, loop)
    if releasedButton(0, click, prev_click) and mouseinRange(mouse, btn_next_rect.left, btn_next_rect.right, btn_next_rect.top + controlbar_up, btn_next_rect.bottom + controlbar_up):
        music_cntr = changeMusic(music_cntr, 0, len(music), dir, music, randomOn, loop)
    # режим повтора
    if releasedButton(0, click, prev_click) and mouseinRange(mouse, btn_loop_rect.left, btn_loop_rect.right, btn_loop_rect.top + controlbar_up, btn_loop_rect.bottom + controlbar_up): loop = not loop
    # режим рандома
    if releasedButton(0, click, prev_click) and mouseinRange(mouse, btn_rand_rect.left, btn_rand_rect.right, btn_rand_rect.top + controlbar_up, btn_rand_rect.bottom + controlbar_up): randomOn = not randomOn

    # заливка фона
    screen.fill(bg_clr) 
    controlbar.fill(bar_bg_clr)
    songPicture.fill((20, 20, 30))
    songPicture.blit(emptyPic, emptyPic_rect)  

    # рендер кнопок
    if pause:   controlbar.blit(btn_play, btn_pause_rect)
    else:       controlbar.blit(btn_pause, btn_pause_rect)
    if loop:    controlbar.blit(btn_loopOn, btn_loop_rect)
    else:       controlbar.blit(btn_loopOff, btn_loop_rect)
    if randomOn:controlbar.blit(btn_randOn, btn_rand_rect)
    else:       controlbar.blit(btn_randOff, btn_rand_rect)
    controlbar.blit(btn_next, btn_next_rect)
    controlbar.blit(btn_prev, btn_prev_rect)

    # рендер тектса
    musicNum = smallfont.render(f"{music_cntr+1} / {len(music)}", 1, (244, 244, 244))
    musicNum_rect = musicNum.get_rect()
    musicNum_rect.centerx, musicNum_rect.top = width // 2, height / 50
    screen.blit(musicNum, musicNum_rect)
    musicName = bigfont.render(music[music_cntr], 1, (244, 244, 244))
    musicName_rect = musicName.get_rect()
    musicName_rect.centerx, musicName_rect.top = width // 2, height * 0.575
    screen.blit(musicName, musicName_rect)

    # обновление кадра 
    emptyPic, emptyPic_rect = rotate(emptyPic_copy, angle, emptyPic_rect)
    screen.blit(songPicture, songPicture_rect)
    screen.blit(controlbar, (0, controlbar_up))
    prev_action = action
    prev_click = click
    if not pause: angle+= 0.125
    pygame.display.flip()
    fps.tick(60)