import pygame

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
gravity = 0.75
knightX, knightY = 370, 480

background = pygame.image.load('assets/map/Castlevania_Harmony_of_Dissonance.jpg')
back_ground = pygame.transform.scale(background, (int(background.get_width() * 2), int(background.get_height() * 2)))
#game_font = pygame.font.Font('assets/04B_19.ttf',40)