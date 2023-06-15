import pygame
from constants import screen, gravity

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.health = 100
        self.velocity_y = 0
        self.jump = False
        self.in_air = True
        self.falling = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Idle_stance', 'Staff_Fast_Run', "Dash", "Dash_back", "Fall_Flat", "Front_Flip", "Fall_Land"]
        
        animation_file_numbers = {'Idle_stance': 10, 'Staff_Fast_Run': 6, "Dash": 5,
                                   "Dash_back": 1, "Fall_Flat": 6, "Front_Flip": 8, "Fall_Land": 3}

        for animation in animation_types:
            temp_animation_list = []

            number_of_frames = animation_file_numbers[animation]

            for i in range(number_of_frames):
                knight = pygame.image.load(f'assets/animations/{animation}/{i}.png')
                knight = pygame.transform.scale(knight, (int(knight.get_width() * scale), int(knight.get_height() * scale)))
                temp_animation_list.append(knight)
            self.animation_list.append(temp_animation_list)

        self.knight_image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0,0, 35, 90)
        self.rect.center = (x, y)

    def move(self, move_left, move_right): 
        changeinX = 0
        changeinY = 0
        if move_left:
            changeinX = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            changeinX = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True and self.in_air == False:
            self.velocity_y = -23
            self.jump = False
            self.in_air = True

        self.velocity_y += gravity
        if self.velocity_y > 10:
            self.velocity_y = 10
        changeinY  += self.velocity_y

        if self.rect.bottom + changeinY > 793:
            changeinY = 793 - self.rect.bottom
            self.in_air = False

        self.rect.x += changeinX
        self.rect.y += changeinY    

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.knight_image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index  >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def knight_draw(self):
        screen.blit(pygame.transform.flip(self.knight_image, self.flip, False), (self.rect.x -80, self.rect.y - 28))