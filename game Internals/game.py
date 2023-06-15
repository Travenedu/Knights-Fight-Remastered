import pygame
from constants import FPS, screen, background
from internals.game_internals import Internal
from internals.Map import Background
from internals.character import Knight

#Game Title
pygame.display.set_caption('Kings Fight')

def main():
    running = True
    clock = pygame.time.Clock()
    move_left = False
    move_right = False
    dash_back = False
    dash_forward = True 
    score = 0
    high_score = 0
    game_over = False
    key_timer = 0
    double_click_event = pygame.USEREVENT
    knight1 = Knight(200, 600, 3.2, 5)
    background_castle = Background(-14286, -6190, background, 2, 7)
    
    while running:
        clock.tick(FPS)
        if game_over == False:
            screen.fill((0,0,0))

            #Castle
            # background_castle.move(move_left, move_right)
            # background_castle.background_draw()

            #knight
            knight1.update_animation()
            knight1.knight_draw()            

            #animation select
            if knight1.alive:
                if knight1.in_air:
                    knight1.update_action(1)#need jump animation

                elif move_left or move_right:
                    # Run Fast with staff
                    knight1.update_action(1)
                elif True:
                    # Dash forward
                    knight1.update_action(2)
                elif True:
                    # Dash Backwords
                    knight1.update_action(3)
                elif True:
                    # Fall flat on Face
                    knight1.update_action(4)
                elif True:
                    # Front flip
                    knight1.update_action(5)
                elif True:
                    # Fall Landing 
                    knight1.update_action(5)
                else:
                    # Idle Stance
                    knight1.update_action(0)
                knight1.move(move_left, move_right)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #knight movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if key_timer == 0:
                            pygame.time.set(double_click_event, 500)
                            timerset = True
                            dash_left = True
                        else:
                            move_left = True
                    if event.key == pygame.K_d:
                        if key_timer == 0:
                            pygame.time.set(double_click_event, 500)
                            timerset = True
                            dash_left = True
                        else:
                            move_right = True
                    if event.key == pygame.K_SPACE or event.key == pygame.K_w and knight1.alive:
                        knight1.jump = True
                    if event.key == pygame.K_ESCAPE:
                        running = False      

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    if event.key == pygame.K_d:
                        move_right = False

            #Knight health check
            if knight1.health == 0:
                game_over = True

            if game_over == True:
                high_score = Internal.update_score(score, high_score)
                Internal.score_display('game_over', score, high_score)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_over = False
                        knight1 = Knight(200, 30, 3, 5)
                        score = 0.5
                        knight1.health = 100        

        pygame.display.update()

    pygame.quit()

main()