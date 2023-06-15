import pygame

class Background:
    def __init__(self, x, y, image, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.velocity_y = 0
        self.jump = False
        self.in_air = True
        
        self.background_image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = pygame.Rect(0,0, 35, 90)
        self.rect.center = (x, y)