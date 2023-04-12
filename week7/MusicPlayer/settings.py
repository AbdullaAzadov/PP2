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
songPicture = pygame.Surface((width * 0.667, height//2))
songPicture_rect = songPicture.get_rect()
songPicture_rect.centerx = width / 2
songPicture_rect.top = int(screen.get_height() / 16)
controlbar_up = height - controlbar.get_height()
prev_action = pygame.key.get_pressed()
prev_click = pygame.mouse.get_pressed()
randomOn = False
loop = False
pause = False
angle = 1
# Текст
smallfont = pygame.font.Font(None, int(screen.get_height() / 20))
bigfont = pygame.font.Font(None, int(screen.get_height() / 17))

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