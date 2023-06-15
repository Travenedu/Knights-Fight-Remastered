import pygame
from constants import screen, WIDTH


class Internal:
    def __init__(self, postionx, positiony):
        self.postionX = postionx
        self.postionY = positiony

    def score():
        pass



    def move(self, move_left, move_right):  
            changeinX = 0
            changeinY = 0
            if move_left:
                changeinX = self.speed
                self.direction = -1
            if move_right:
                changeinX = -self.speed
                self.direction = 1

            if self.jump == True and self.in_air == False:
                self.velocity_y = -13
                self.jump = False
                self.in_air = True

            #self.velocity_y += Gravity
            if self.velocity_y > 10:
                self.velocity_y = 10
            changeinY  += self.velocity_y

            if self.rect.bottom + changeinY > 793:
                changeinY = 793 - self.rect.bottom
                self.in_air = False

            self.rect.x += changeinX
            self.rect.y += changeinY
            print(self.rect.x)
            print(self.rect.y)

    def background_draw(self):
        screen.blit(self.background_image, (self.rect.x -80, self.rect.y - 28))


