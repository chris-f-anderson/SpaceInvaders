# Ctrl + Shift + P, then select interpreter
# Choose an interpreter that works
import pygame

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((400, 600))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('SPACE INVADERS!')



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.is_alive = False
        elif event.type == pygame.KEYDOWN:
            key_left = event.key in (pygame.K_LEFT, pygame.K_a)
            key_right = event.key in (pygame.K_RIGHT, pygame.K_d)
            key_up = event.key in (pygame.K_UP, pygame.K_w)
            key_down = event.key in (pygame.K_DOWN, pygame.K_s)
            if key_left:
                snake.set_direction_left()
            elif key_right:
                snake.set_direction_right()

    # Main game loop
    is_playing = True
    while is_playing:
        game_display.blit(game_display, (0, 0))
        
        game_display.fill((0, 0, 0))
        pygame.draw.rect(game_display, (0 , 255, 0), pygame.Rect(50, 50, 20, 20))
        # score_text = score_font.render(str(snake.score), False, (255, 255, 255))
        # game_display.blit(score_text, (0,0))

        pygame.display.update()

        clock.tick(30)
pygame.quit()
