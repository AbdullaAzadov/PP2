import pygame, os

# Инициализация
pygame.init()
pygame.mixer.init()
dir = "C:/pp2/week7/MusicPlayer/"

# Создаем окно
width = 480
height = 640
fps = pygame.time.Clock()
pygame.display.set_caption("Music Player")
screen = pygame.display.set_mode((width, height))
controlbar = pygame.Surface((width, height//3))
controlbar_rect = controlbar.get_rect()
prev_action = pygame.key.get_pressed()
randomOn = False
loop = False
pause = False

# Цвета
bg_clr = (50, 50, 75)
bar_bg_clr = (25, 25, 50)

# Подгружаем песни
files = os.listdir(dir + "music/")
music = []
music_cntr = 0
for file in files:
    if file.endswith(".mp3") or file.endswith(".ogg"):
        music.append(file)
pygame.mixer.music.load(dir + "music//" + music[music_cntr])
pygame.mixer.music.play()